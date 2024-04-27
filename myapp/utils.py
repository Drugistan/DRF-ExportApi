import csv
import random
from django.core.management.base import BaseCommand
from django.http import HttpResponse
# from faker import Faker
from .models import Order


# def handle():
#     fake = Faker()
#     for _ in range(10):  # Adjust the number of dummy records as needed
#         Order.objects.create(
#             name=fake.name(),
#             address=fake.address(),
#             phone=fake.phone_number(),
#             age=random.uniform(10.0, 100.0),
#             # Add more fields and generate data as needed
#         )


class ExportExcel(object):

    def __init__(self):
        self.status = None
        self.queryset = Order.objects.all()
        self.response = HttpResponse(content_type='text/csv')
        self.response['Content-Disposition'] = 'attachment; filename="orders_export.csv"'
        self.writer = csv.writer(self.response)
        self.create_header()

    def create_header(self):
        self.writer.writerow(
            [
                "name",
                "phone",
                "address",
                "age"
            ]
        )

    def get_data(self):

        if self.queryset:

            for order in self.queryset:
                self.writer.writerow(
                    [order.name, order.phone, order.address, order.age]
                )
                self.status = True
        return self.status, self.response
