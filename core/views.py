from rest_framework import viewsets, filters
from .models import Transaction, TellerSession, Task
from .serializers import TransactionSerializer, TellerSessionSerializer, TaskSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['transaction_type', 'description']

class TellerSessionViewSet(viewsets.ModelViewSet):
    queryset = TellerSession.objects.all()
    serializer_class = TellerSessionSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
