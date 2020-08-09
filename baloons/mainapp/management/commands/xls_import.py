from django.core.management import BaseCommand
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser
import openpyxl


def open_xls_file(path):
    try:
        wb = openpyxl.load_workbook(path)
        print(f'file {path} opened')
        ws = wb.active
        return ws
    except FileNotFoundError as e:
        print(e)
        return e


def xls_import_products(path):
    """ Provide a path to an xslx file with products - get it imported to the DB """
    ws = open_xls_file(path)
    if not isinstance(ws, FileNotFoundError):
        for row in ws.iter_rows(min_row=2, values_only=True):
            category = category_check(row[6])
            # category = ProductCategory.objects.filter(id=row[6])[0]
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


def category_check(category_name: str):
    """ checks if category is in DB and creates one if not """
    category = ProductCategory.objects.filter(name=category_name)
    try:
        return category[0]
    except IndexError:
        new_category = ProductCategory(name=category_name)
        new_category.save()
        return new_category


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--path", required=True, type=str)

    def handle(self, path, **options):
        xls_import_products(path)
        ShopUser.objects.create_superuser('django', 'kotnors@mail.ru', 'geekbrains', age=90)


