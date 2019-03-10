from rest_framework import serializers
from .models import TranslateHistory
# import datetime

class TranslateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslateHistory
        fields = '__all__'
