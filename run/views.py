import io
import csv

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, F, FloatField

from order.models import Order
from .models import Run


def manifest_view(request, run_id):
    run = get_object_or_404(Run, id=run_id)
    orders = Order.objects.filter(run=run, canceled=False).order_by('sequence')
    manifest_orders = []
    for order in orders:
        order.volume = sum([product.quantity * product.product.meterage for product in order.orderproduct.all()])
        manifest_orders.append(order)

    return render(request, 'run/manifest.html', {'run': run, 'orders': manifest_orders})


def job_export_view(request, run_id):
    run = get_object_or_404(Run, id=run_id)
    orders = Order.objects.filter(run=run, canceled=False, booked=False).order_by('sequence')

    rows = [['DATE', 'ACCT', 'REF 1', 'REF 2', 'SERVICE', '# ITEMS', 'CUSTOMER', 'ADDRESS LINE 1', 'ADDRESS LINE 2',
             'ADDRESS LINE 3', 'ADDRESS LINE 4', 'SUBURB', 'PRICE', 'DRIVER']]

    for order in orders:
        quantity = sum([product.quantity for product in order.orderproduct.all()])
        volume = sum([product.quantity * product.product.meterage for product in order.orderproduct.all()])
        price = round((order.price or 0.0) / 1.1 * 100)

        rows.append([
            run.delivery_date.strftime('%d/%m/%Y'),
            '8756D',
            order.reference,
            'Run {0} Job {1}'.format(run_id, order.id),
            'FQT',
            quantity,
            order.name,
            order.address1,
            order.address2,
            'VOL: {0}m3 QTY:{1} items'.format(volume, quantity),
            run.name,
            order.suburb.name,
            price,
            run.driver.driver_number
        ])

    string_buffer = io.StringIO()
    csv_writer = csv.writer(string_buffer)
    csv_writer.writerows(rows)

    return HttpResponse(string_buffer.getvalue(), content_type='text/plain')


def invoice_export_view(request, run_id):
    run = get_object_or_404(Run, id=run_id)
    orders = Order.objects.filter(run=run, canceled=False).order_by('sequence')

    total_price = sum([order.price for order in orders])
    price = round((total_price or 0.0) / 1.1 * 100)

    rows = [['DATE', 'ACCT', 'REF 1', 'REF 2', 'SERVICE', '# ITEMS', 'CUSTOMER', 'ADDRESS LINE 1', 'ADDRESS LINE 2', 'ADDRESS LINE 3', 'ADDRESS LINE 4', 'SUBURB', 'PRICE', 'DRIVER']]

    rows.append([
        run.delivery_date.strftime('%d/%m/%Y'),
        '8756',
        'Run {0}'.format(run_id),
        '{0} - {1}'.format(run.delivery_date.strftime('%d/%m/%Y'), run.name),
        'FQT',
        0,
        'Warehouse Furniture Clearance',
        run.name,
        'Run: {0} Driver: {1}'.format(run.id, run.driver.driver_number),
        '',
        'Albany Creek',
        price,
        run.driver.driver_number
    ])

    string_buffer = io.StringIO()
    csv_writer = csv.writer(string_buffer)
    csv_writer.writerows(rows)

    return HttpResponse(string_buffer.getvalue(), content_type='text/plain')