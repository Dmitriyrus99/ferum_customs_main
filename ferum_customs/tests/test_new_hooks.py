import os

import pytest

pytest.importorskip("frappe")

import frappe  # noqa: E402
from frappe.tests.utils import FrappeTestCase  # noqa: E402

from ferum_customs.custom_logic import service_report_hooks, service_request_hooks


class DummyLogger:
    def __init__(self):
        self.messages = []

    def info(self, msg):
        self.messages.append(msg)


class TestNewHooks(FrappeTestCase):
    TEST_SITE = os.environ.get("SITE_NAME", getattr(frappe.local, "site", None))

    def test_after_insert_request(self, monkeypatch, frappe_site):
        logger = DummyLogger()
        monkeypatch.setattr(frappe, "logger", lambda *a, **k: logger)
        doc = frappe._dict(name="REQ-1")
        service_request_hooks.after_insert(doc)
        self.assertIn("REQ-1", logger.messages[0])

    def test_after_insert_report(self, monkeypatch, frappe_site):
        logger = DummyLogger()
        monkeypatch.setattr(frappe, "logger", lambda *a, **k: logger)
        doc = frappe._dict(name="REP-1")
        service_report_hooks.after_insert(doc)
        self.assertIn("REP-1", logger.messages[0])

