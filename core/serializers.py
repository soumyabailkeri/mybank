from rest_framework import serializers
from .models import Transaction, TellerSession

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TellerSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TellerSession
        fields = '__all__'