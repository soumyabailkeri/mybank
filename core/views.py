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
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'is_completed']

    def get_queryset(self):
        queryset = Task.objects.all()
        is_completed = self.request.query_params.get('is_completed')
        if is_completed is not None:
            is_completed = is_completed.lower() == 'true'
            queryset = queryset.filter(is_completed=is_completed)
        return queryset

