from rest_framework import viewsets, filters
from .models import Transaction, TellerSession
from .serializers import TransactionSerializer, TellerSessionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['transaction_type', 'description']

class TellerSessionViewSet(viewsets.ModelViewSet):
    queryset = TellerSession.objects.all()
    serializer_class = TellerSessionSerializer