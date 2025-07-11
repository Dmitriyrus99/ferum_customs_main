"""DocType hook mapping used by hooks.py."""

DOC_EVENTS = {
    "Service Request": {
        "validate": "ferum_customs.custom_logic.service_request_hooks.validate",
        "on_update_after_submit": "ferum_customs.custom_logic.service_request_hooks.on_update_after_submit",
        "on_trash": "ferum_customs.custom_logic.service_request_hooks.prevent_deletion_with_links",
        "after_insert": "ferum_customs.custom_logic.service_request_hooks.after_insert",
        "on_cancel": "ferum_customs.custom_logic.service_request_hooks.on_cancel",
    },
    "Service Report": {
        "validate": "ferum_customs.custom_logic.service_report_hooks.validate",
        "on_submit": "ferum_customs.custom_logic.service_report_hooks.on_submit",
        "after_insert": "ferum_customs.custom_logic.service_report_hooks.after_insert",
        "on_cancel": "ferum_customs.custom_logic.service_report_hooks.on_cancel",
    },
    "Service Object": {
        "validate": "ferum_customs.custom_logic.service_object_hooks.validate",
    },
    "Payroll Entry Custom": {
        "validate": "ferum_customs.custom_logic.payroll_entry_hooks.validate",
        "before_save": "ferum_customs.custom_logic.payroll_entry_hooks.before_save",
    },
    "Custom Attachment": {
        "on_trash": "ferum_customs.custom_logic.file_attachment_utils.on_custom_attachment_trash",
    },
}
