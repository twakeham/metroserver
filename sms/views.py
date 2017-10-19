from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Q

from twilio.twiml.messaging_response import MessagingResponse

from order.models import Order, Flags
from user.models import User

from .models import Message


SYSTEM = User.objects.get(username='SYSTEM')


@csrf_exempt
def reply_to_sms_messages(request):
    r = MessagingResponse()
    from_ = request.POST['From']
    body = request.POST['Body'].strip()

    phone = from_.replace('+61', '0').strip()
    print(phone)

    orders = Order.objects.filter(phone1=phone, canceled=False, completed=False)#(completed=False).filter(Q(phone1=phone) | Q(phone2=phone))
    print(orders)

    # check for duplicate orders and flag them
    if len(orders) > 1:
        print('Duplicate orders')
        for order in orders:
            Message.objects.create(user=SYSTEM, phone=phone, text=body, sent=False, order=order)
            Flags.objects.create(order=order, acknowledged=False, text='Duplicate orders found with caller id - no action has been taken')

        r.message('Thank-you for your response. We will be in touch shortly.')
        return HttpResponse(r.to_xml(), content_type='text/xml')

    elif not orders:
        print('Order not found')
        Message.objects.create(user=SYSTEM, phone=phone, text=body, sent=False, order=None)
        return HttpResponse(r.to_xml(), content_type='text/xml')

    else:
        order = orders[0]

        # we're at the selecting preferred day stage
        if not order.preferred_day:
            print('Already set preferred day')
            Message.objects.create(user=SYSTEM, phone=phone, text=body, sent=False, order=order)
            if len(body) != 1:
                print('More than one character returned')
                Flags.objects.create(order=order, acknowledged=False,
                                     text='Unable to decode message reply')
                r.message('Thank-you for your response. We will be in touch shortly.')
                Message.objects.create(user=SYSTEM, phone=phone, text='Thank-you for your response. We will be in touch shortly.', sent=True, order=order)
                return HttpResponse(r.to_xml(), content_type='text/xml')
            else:
                try:
                    option = int(body)
                except ValueError:
                    print('Non numeric reply')
                    Flags.objects.create(order=order, acknowledged=False,
                                         text='Unable to decode message reply')
                    r.message('Thank-you for your response. We will be in touch shortly.')
                    Message.objects.create(user=SYSTEM, phone=phone,
                                           text='Thank-you for your response. We will be in touch shortly.', sent=True,
                                           order=order)
                    return HttpResponse(r.to_xml(), content_type='text/xml')

                index = 1
                days = {}
                zone = order.suburb.zone

                if zone.monday:
                    days[index] = 'Monday'
                    index += 1

                if zone.tuesday:
                    days[index] = 'Tuesday'
                    index += 1

                if zone.wednesday:
                    days[index] = 'Wednesday'
                    index += 1

                if zone.thursday:
                    days[index] = 'Thursday'
                    index += 1

                if zone.friday:
                    days[index] = 'Friday'
                    index += 1

                if zone.saturday:
                    days[index] = 'Saturday'
                    index += 1

                if zone.sunday:
                    days[index] = 'Sunday'
                    index += 1

                # -- valid response
                if option in days:
                    print('Found the correct day!!!')
                    order.preferred_day = days[option]
                    order.save()

                    r.message('Thank-you for indicating your preference for a {0} delivery. We will be in touch shortly to arrange a delivery date.'.format(days[option]))
                    Message.objects.create(user=SYSTEM, phone=phone,
                                           text='Thank-you for indicating your preference for a {0} delivery. We will be in touch shortly to arrange a delivery date.'.format(days[option]), sent=True,
                                           order=order)
                    return HttpResponse(r.to_xml(), content_type='text/xml')

                else:
                    print('Option selected is not an applicable day')
                    Flags.objects.create(order=order, acknowledged=False,
                                         text='Client selected an unavailable day')
                    r.message('Thank-you for your response. We will be in touch shortly.')
                    Message.objects.create(user=SYSTEM, phone=phone,
                                           text='Thank-you for your response. We will be in touch shortly.', sent=True,
                                           order=order)
                    return HttpResponse(r.to_xml(), content_type='text/xml')

        # -- stuff other than choosing a day
        else:
            Message.objects.create(user=SYSTEM, phone=phone, text=body, sent=False, order=order)
            Flags.objects.create(order=order, acknowledged=False,
                                 text='Client replied to unspecified prompt')

            return HttpResponse(r.to_xml(), content_type='text/xml')

    return HttpResponse(r.to_xml(), content_type='text/xml')



    # r.message('{0}\n{1}'.format(from_, body))
    # return HttpResponse(r.to_xml(), content_type='text/xml')