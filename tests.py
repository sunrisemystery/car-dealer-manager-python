"""Tests for modules: customersRegister.py and cars_db.py"""
import unittest
import tkinter
import customersRegister
import cars_db


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


class CarDBTest(unittest.TestCase):
    """Tests for some functions in CarsDatabase class."""

    def setUp(self) -> None:
        self.car_db = cars_db.CarsDatabase(':memory:')
        self.car_db.insert("Audi", "A1", "Blue", 2003, 25000)

    def test_fetch_brand(self):
        row = self.car_db.fetch()
        self.assertEqual(row[0][1], "Audi")

    def test_fetch_model(self):
        row = self.car_db.fetch()
        self.assertEqual(row[0][2], "A1")

    def test_fetch_color(self):
        row = self.car_db.fetch()
        self.assertEqual(row[0][3], "Blue")

    def test_fetch_year(self):
        row = self.car_db.fetch()
        self.assertEqual(row[0][4], 2003)

    def test_fetch_price(self):
        row = self.car_db.fetch()
        self.assertEqual(row[0][6], 25000)

    def test_default_instock_value(self):
        row = self.car_db.isout(1)
        self.assertEqual(row[0], 1)

    def test_available(self):
        row = self.car_db.fetch_available()
        self.assertEqual(row[0][1], "Audi")

    def test_out_of_stock(self):
        self.car_db.outofstock(1)
        row = self.car_db.isout(1)
        self.assertEqual(row[0], 0)


if __name__ == '__main__':
    unittest.main()
