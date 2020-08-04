from django.core.management import BaseCommand
from mainapp.models import Product, ProductCategory
import openpyxl


def xls_import(path):
    """ Provide a path to an xslx file with products - get it imported to the DB """
    try:
        wb = openpyxl.load_workbook(path)
        print(f'file {path} opened')
        ws = wb.active
        for row in ws.iter_rows(min_row=2, values_only=True):
            category = ProductCategory.objects.filter(id=row[6])[0]
            params = {
                      'name': row[0],
                      'image': row[1],
                      'short_desc': row[2],
                      'description': row[3],
                      'price': row[4],
                      'quantity': row[5],
                      'category': category
                      }
            print(f'Adding new product: \n {params}')
            new_product = Product(**params)
            new_product.save()
    except FileNotFoundError as e:
        print(e)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--path", required=True, type=str)

    def handle(self, path, **options):
        xls_import(path)

