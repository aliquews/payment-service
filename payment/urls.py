from django.urls import path

from .views import ItemView, buy_item


urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='detail-item'),
    path('buy/<int:pk>', buy_item, name='buy-item'),
]