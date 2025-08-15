from rest_framework import viewsets, permissions, generics, filters, serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'location']
    filterset_fields = ['date']

class TicketPurchaseView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        quantity = serializer.validated_data['quantity']
        if event.available_tickets < quantity:
            raise serializers.ValidationError("Not enough tickets available. Browse for other shows you might like")
        event.available_tickets -= quantity
        event.price = quantity * event.price
        event.save()
        serializer.save(user=self.request.user)
        # return price * quantity 

class MyTicketsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)
    