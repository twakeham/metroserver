from geopy import geocoders, exc

from PyQt5.QtCore import QThread
from PyQt5.QtSql import QSqlQuery

import objects
import order

from order.models import OrderModel
from order.flag.models import FlagModel


def geolocate(order_id: int):
    model = OrderModel()
    flags = FlagModel()
    flags.select()
    model.setFilter('id={0}'.format(order_id))
    model.select()
    record = model.record(0)

    if not record.value('id'):
        return False

    address1 = record.value('address1')
    address2 = record.value('address2')
    suburb = record.value('suburb_id')
    if not address2:
        address = '{0}, {1}, Australia'.format(address1, suburb)
    else:
        address = '{0}, {1}, {2}, Australia'.format(address1, address2, suburb)

    geolocator = geocoders.GoogleV3(api_key='AIzaSyAGiVHm_ia8cfkJ2MBtiAAGDAPJjop77Dk')
    try:
        location = geolocator.geocode(address)
    except exc.GeocoderTimedOut:
        flags.create_flag(order_id, 'Geolocator timeout')

    if not location:
        flags.create_flag(order_id, 'Unable to geolocate address, please check')
        return False

    model.set_data(0, latitude=location.latitude, longitude=location.longitude)
    return model.submitAll()


if __name__ == '__main__':
    import sys

    try:
        fn, id = sys.argv
    except:
        sys.exit(1)

    try:
        id = int(id)
    except ValueError:
        sys.exit(1)

    geolocate(id)