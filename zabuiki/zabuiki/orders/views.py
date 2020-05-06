
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from yandex_money.forms import PaymentForm
from yandex_money.models import Payment

from zabuiki.events.models import Event
from zabuiki.orders.models import Order
from zabuiki.views import get_main_context


def order_event(request, event_id):
    context = get_main_context(request)
    event = get_object_or_404(Event, id=event_id)
    amount = event.price
    print (event.price)
    payment = Payment(order_amount=amount)
    payment.save()

    order = Order(product=event, payment=payment, amount=amount)
    order.save()

    context.update({
        'form': PaymentForm(instance=payment),
    })

    return render(request, "order.html", context=context)
