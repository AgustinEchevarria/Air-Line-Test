import unittest
from datetime import date
from service import AirLine, Client, Package


def main():
    airline = AirLine()
    unittest.main(exit=False)
    while True:
        action = input("Enter 'transport' to transport a package or 'report' to generate a report (or 'exit' to quit): ")

        if action == 'exit':
            break

        elif action == 'transport':
            client_name = input("Enter client name: ")
            package_id = input("Enter package ID: ")
            transport_date_str = input("Enter transport date (YYYY-MM-DD): ")

            try:
                client = Client(client_name)
                package = Package(package_id, client)
                transport_date = date.fromisoformat(transport_date_str)
                airline.transport(package, transport_date)
                print(f"Package {package_id} for client {client_name} was successfully transported on {transport_date_str}.")

            except ValueError as e:
                print(f"Error: {e}")

        elif action == 'report':
            report_date_str = input("Enter report date (YYYY-MM-DD): ")

            try:
                report_date = date.fromisoformat(report_date_str)
                report = airline.generate_report(report_date)
                print(f"Report for {report_date}:")
                print(f"Total packages: {report['total_packages']}")
                print(f"Total amount: {report['total_amount']}")

            except ValueError as e:
                print(f"Error: {e}")

        else:
            print("Invalid action. Please try again.")


if __name__ == '__main__':
    main()


