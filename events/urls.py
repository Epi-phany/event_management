from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TicketPurchaseView, MyTicketsView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('buy-ticket/', TicketPurchaseView.as_view(), name='buy-ticket'),
    path('my-tickets/', MyTicketsView.as_view(), name='my-tickets'),
]