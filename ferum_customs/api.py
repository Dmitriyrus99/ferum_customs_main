from typing import Optional

import frappe
from frappe import _, whitelist
from frappe.exceptions import PermissionError


@whitelist()
def validate_service_request(docname: str) -> Optional[dict]:
    """Return the service request document as a dict after permission check."""
    if not frappe.has_permission("Service Request", "read"):
        frappe.throw(_("Not permitted"), PermissionError)

    try:
        doc = frappe.get_doc("Service Request", docname)
        return doc.as_dict()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Error validating Service Request")
        raise


@whitelist()
def on_submit_service_request(docname: str) -> None:
    """Hook executed when a Service Request is submitted."""
    frappe.logger(__name__).info(f"Service Request '{docname}' submitted")


@whitelist()
def cancel_service_request(docname: str) -> None:
    """Hook executed when a Service Request is cancelled."""
    frappe.logger(__name__).info(f"Service Request '{docname}' cancelled")


@whitelist()
def validate_service_report(docname: str) -> Optional[dict]:
    """Return the service report document as a dict after permission check."""
    if not frappe.has_permission("Service Report", "read"):
        frappe.throw(_("Not permitted"), PermissionError)

    try:
        doc = frappe.get_doc("Service Report", docname)
        return doc.as_dict()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Error validating Service Report")
        raise


@whitelist()
def on_submit_service_report(docname: str) -> None:
    """Hook executed when a Service Report is submitted."""
    frappe.logger(__name__).info(f"Service Report '{docname}' submitted")


@whitelist()
def create_invoice_from_report(service_report: str) -> str:
    """Create a Sales Invoice draft from a submitted Service Report.

    Args:
        service_report: ID of the Service Report document.

    Returns:
        The name of the created Sales Invoice document.
    """
    if not service_report:
        frappe.throw(_("Service Report ID is required"))

    if frappe.db.exists(
        "Sales Invoice", {"service_report": service_report, "docstatus": ["<", 2]}
    ):
        frappe.throw(_("Sales Invoice already exists for this Service Report."))

    sr = frappe.get_doc("Service Report", service_report)

    invoice = frappe.get_doc(
        {
            "doctype": "Sales Invoice",
            "customer": sr.get("customer"),
            "service_report": service_report,
            "items": [],
        }
    )

    for item in sr.get("work_items", []):
        invoice.append(
            "items",
            {
                "description": item.get("description"),
                "qty": item.get("quantity"),
                "rate": item.get("unit_price"),
                "amount": item.get("amount"),
            },
        )

    invoice.insert(ignore_permissions=True)
    return invoice.name


@whitelist()
def get_request_status(docname: str) -> Optional[str]:
    """Return status of the given Service Request."""
    return frappe.db.get_value("Service Request", docname, "status")


@whitelist()
def get_report_status(docname: str) -> Optional[str]:
    """Return status of the given Service Report."""
    return frappe.db.get_value("Service Report", docname, "status")


@whitelist()
def generate_pdf(doctype: str, docname: str, print_format: str | None = None) -> bytes:
    """Return PDF bytes for the specified document using a print format."""
    return frappe.get_print(doctype, docname, print_format=print_format, as_pdf=True)


@whitelist()
def create_pdf_attachment(
    doctype: str, docname: str, print_format: str | None = None
) -> str:
    """Generate PDF attachment from template and attach to the document."""
    pdf = generate_pdf(doctype, docname, print_format)
    file_doc = frappe.get_doc(
        {
            "doctype": "File",
            "file_name": f"{doctype}-{docname}.pdf",
            "content": pdf,
            "attached_to_doctype": doctype,
            "attached_to_name": docname,
        }
    ).insert(ignore_permissions=True)
    return file_doc.file_url
