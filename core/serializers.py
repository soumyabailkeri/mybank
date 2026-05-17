from rest_framework import serializers
from .models import Transaction, TellerSession, Task

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TellerSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TellerSession
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


