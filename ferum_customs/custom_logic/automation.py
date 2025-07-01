"""Automation helpers for engineer assignment and SLA checks."""

from __future__ import annotations

import frappe


def assign_engineers_by_zone(doc, method: str | None = None) -> None:
    """Assign engineers based on the service object's zone."""
    zone = doc.get("zone")
    if not zone:
        return

    engineers = frappe.get_all(
        "Employee",
        filters={"zone": zone},
        pluck="user_id",
    )

    for engineer in engineers:
        doc.append("assigned_engineers", {"engineer": engineer})


def remind_due_dates() -> None:
    """Send reminders about approaching due dates for open requests."""
    open_requests = frappe.get_all(
        "Service Request",
        filters={"status": ["not in", ["Closed", "Cancelled"]]},
        fields=["name", "expected_end_date", "custom_assigned_engineer"],
    )

    for req in open_requests:
        if req.expected_end_date and req.expected_end_date <= frappe.utils.today():
            frappe.sendmail(
                recipients=[req.custom_assigned_engineer],
                subject=f"Reminder for {req.name}",
                message="Service Request is due",
            )


def check_sla(doc, method: str | None = None) -> None:
    """Warn if the response time exceeds the contract SLA."""
    sla = frappe.db.get_value("Service Contract", doc.get("service_contract"), "sla")
    if sla and doc.get("response_time") and doc.response_time > sla:
        frappe.msgprint("SLA breach detected", alert=True)
