"""Tests for modules: customersRegister.py and cars_db.py"""
import unittest
import tkinter

import customersRegister


class RegisterTest(unittest.TestCase):
    """Tests for clear_text function in CustomerRegister class."""

    def setUp(self) -> None:
        self.customer = customersRegister.CustomerRegister(tkinter.Tk())
        self.customer.init_window()

    def test_clear_access_key(self):
        self.customer.access_key_entry.insert(0, "value")
        self.customer.clear_text()
        self.assertFalse(self.customer.access_key_entry.get() == "value")

    def test_clear_name(self):
        self.customer.name_entry.insert(0, "value")
        self.customer.clear_text()
        self.assertFalse(self.customer.name_entry.get() == "value")

    def test_clear_lastname(self):
        self.customer.lastname_entry.insert(0, "value")
        self.customer.clear_text()
        self.assertFalse(self.customer.lastname_entry.get() == "value")

    def test_clear_email(self):
        self.customer.email_entry.insert(0, "value")
        self.customer.clear_text()
        self.assertFalse(self.customer.email_entry.get() == "value")

    def test_clear_phone_number(self):
        self.customer.phone_entry.insert(0, "value")
        self.customer.clear_text()
        self.assertNotEqual(self.customer.phone_entry.get(), "value")


if __name__ == '__main__':
    unittest.main()
