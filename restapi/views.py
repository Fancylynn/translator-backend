from django.shortcuts import render
from .models import TranslateHistory
from .serializers import TranslateHistorySerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Imports the Google Cloud client library
from google.cloud import translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"
import datetime
import six

# Create your views here.
class TranslatorViewSet(viewsets.ModelViewSet):
    queryset = TranslateHistory.objects.all()
    serializer_class = TranslateHistorySerializer
    http_method_names = ['get', 'post']

    # Get all the translation history
    def list(self, request):
        queryset = TranslateHistory.objects.all()
        serializer = TranslateHistorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    # Get a specific translation record
    def retrieve(self, request, pk=None):
        queryset = TranslateHistory.objects.get(id=pk)
        serializer = TranslateHistorySerializer(queryset)
        return Response(serializer.data)
    
    def create(self, request):     
        input_text = request.POST.get('input_text')
        # Do google translation
        translation = self.googleTranslate(input_text)

        new_translation = TranslateHistory.objects.create(
            input_text = input_text,
            language = translation['detectedSourceLanguage'],
            translation = translation['translatedText'],
            timestamp = datetime.datetime.now()
        )

        new_translation.save()
        return Response(data=TranslateHistorySerializer(new_translation).data)

    def googleTranslate(self, text):
        # Instantiates a client
        translate_client = translate.Client()
        # if isinstance(text, six.binary_type):
        #     text = text.decode('utf-8')
        
        print(text)
        # translate_client = translate_client.from_service_account_json(os.path.abspath('../apikey.json'))
        translation = translate_client.translate(text, target_language='en')
        return translation
