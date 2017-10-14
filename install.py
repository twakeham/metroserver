import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metroserver.settings")
django.setup()

import csv

## -- INSTALL SUBURBS
# from suburb.models import *
#
# with open('c:\\suburbs.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     data = list(reader)
#
# zones = {}
#
#
# for line in data:
#     postcode, suburb, zone, mon, tues, wed, thu, fri, sat, sun = line
#     monday = mon == 'TRUE'
#     tuesday = tues == 'TRUE'
#     wednesday = wed == 'TRUE'
#     thursday = thu == 'TRUE'
#     friday = fri == 'TRUE'
#     saturday = sat == 'TRUE'
#     sunday = sun == 'TRUE'
#     zone_name = zone.title()
#     if zone_name not in zones:
#         zones[zone_name] = Zone.objects.get_or_create(name=zone_name, monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday, friday=friday, saturday=saturday, sunday=sunday)[0]
#     zone_object = zones[zone_name]
#     try:
#         suburb_object = Suburb.objects.get_or_create(name=suburb.title(), zone=zone_object)
#     except:
#         print(suburb, postcode)


from product.models import *

with open('c:\\products.csv') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)

for line in data:
    code, description, meterage = line
    Product.objects.create(code=code, description=description, meterage=float(meterage))
