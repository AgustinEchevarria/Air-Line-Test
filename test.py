import unittest
from service import AirLine, Client, Package
from datetime import date


class TestAirLine(unittest.TestCase):
    def setUp(self):
        self.airline = AirLine()
        self.client1 = Client("Juan Perez")
        self.client2 = Client("María Gómez")
        self.package1 = Package("PKG001", self.client1)
        self.package2 = Package("PKG002", self.client2)
        self.package3 = Package("PKG003", self.client1)

    def test_transport_package(self):
        self.airline.transport(self.package1, date(2023, 6, 7))
        self.airline.transport(self.package2, date(2023, 6, 7))
        self.assertEqual(len(self.airline.packages_transported[date(2023, 6, 7)]), 2)

    def test_generate_report(self):
        self.airline.transport(self.package1, date(2023, 6, 7))
        self.airline.transport(self.package2, date(2023, 6, 7))
        self.airline.transport(self.package3, date(2023, 6, 8))

        report_june_7 = self.airline.generate_report(date(2023, 6, 7))
        report_june_8 = self.airline.generate_report(date(2023, 6, 8))

        self.assertEqual(report_june_7, {
            'date': date(2023, 6, 7),
            'total_packages': 2,
            'total_amount': '$20'
        })

        self.assertEqual(report_june_8, {
            'date': date(2023, 6, 8),
            'total_packages': 1,
            'total_amount': '$10'
        })

    def test_invalid_package(self):
        with self.assertRaises(ValueError):
            self.airline.transport("Invalid package", date(2023, 6, 7))

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            self.airline.transport(self.package1, "2023-06-07")
            self.airline.generate_report("2023-06-07")

    def test_no_packages_transported(self):
        report = self.airline.generate_report(date(2023, 6, 7))
        self.assertEqual(report, {
            'date': date(2023, 6, 7),
            'total_packages': 0,
            'total_amount': '$0'
        })
