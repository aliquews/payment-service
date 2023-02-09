from django.shortcuts import render
from django.db.models.manager import BaseManager
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe

from .models import Item

# Create your views here.

# секрет
stripe.api_key = 'sk_test_51MZVYqJQbAeSAi2EtqNwzKGiUY30Yntw738VICJbzI2YzjntrkM6k9ko1Mhznb3U48NMSzsaS2jkfLEgRFHO9xF300JeAjBIqK'


class ItemView(DetailView):
    template_name = "index.html"
    context_object_name = "item"
    model = Item


@api_view(['GET'])
def buy_item(request, pk):
    # item: None | BaseManager[Item]
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    session = stripe.checkout.Session.create(
        line_items = [
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': 100*item.price,
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://stripe.com',
        cancel_url='http://google.com/',
    )

    return HttpResponseRedirect(redirect_to=session.url)
