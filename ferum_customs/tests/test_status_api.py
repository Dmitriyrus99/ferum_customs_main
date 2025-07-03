import os

import pytest

pytest.importorskip("frappe")

import frappe  # noqa: E402
from frappe.tests.utils import FrappeTestCase  # noqa: E402

from ferum_customs import api  # noqa: E402


class TestStatusAPI(FrappeTestCase):
    TEST_SITE = os.environ.get("SITE_NAME", getattr(frappe.local, "site", None))

    def test_get_request_status(self, monkeypatch, frappe_site):
        monkeypatch.setattr(frappe.db, "get_value", lambda *a, **k: "Open")
        status = api.get_request_status("REQ-1")
        self.assertEqual(status, "Open")

    def test_get_report_status(self, monkeypatch, frappe_site):
        monkeypatch.setattr(frappe.db, "get_value", lambda *a, **k: "Draft")
        status = api.get_report_status("REP-1")
        self.assertEqual(status, "Draft")

    def test_get_request_status_missing(self, monkeypatch, frappe_site):
        def raise_missing(*a, **k):
            raise frappe.DoesNotExistError

        monkeypatch.setattr(frappe.db, "get_value", raise_missing)
        with pytest.raises(frappe.DoesNotExistError):
            api.get_request_status("REQ-missing")

    def test_get_report_status_missing(self, monkeypatch, frappe_site):
        def raise_missing(*a, **k):
            raise frappe.DoesNotExistError

        monkeypatch.setattr(frappe.db, "get_value", raise_missing)
        with pytest.raises(frappe.DoesNotExistError):
            api.get_report_status("REP-missing")
