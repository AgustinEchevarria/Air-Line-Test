from datetime import date


class Package:
    def __init__(self, package_id, client):
        if not isinstance(client, Client):
            raise ValueError("The package must have a valid client.")
        self.package_id = package_id
        self.client = client


class Client:
    def __init__(self, name):
        if not name:
            raise ValueError("The name must not be empty")
        self.name = name


class AirLine:
    def __init__(self):
        self.packages_transported = {}
        self.package_fee = 10

    def transport(self, package, transport_date):
        if not isinstance(package, Package):
            raise ValueError("Must carry a valid package.")
        if not isinstance(transport_date, date):
            raise ValueError("Invalid date format")

        if transport_date not in self.packages_transported:
            self.packages_transported[transport_date] = []

        self.packages_transported[transport_date].append(package)

    def generate_report(self, report_date):
        if not isinstance(report_date, date):
            raise ValueError("Invalid date format")

        if report_date not in self.packages_transported:
            return {
                'date': report_date,
                'total_packages': 0,
                'total_amount': '$0'
            }

        total_packages = len(self.packages_transported[report_date])
        total_amount = total_packages * self.package_fee
        return {
            'date': report_date,
            'total_packages': total_packages,
            'total_amount': f'${total_amount}'
        }
