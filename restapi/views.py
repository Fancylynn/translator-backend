from django.shortcuts import render
from .models import TranslateHistory
from .serializers import TranslateHistorySerializer
from rest_framework import viewsets, status
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
        try:
            queryset = TranslateHistory.objects.get(id=pk)
        except:
            return Response('The target translation does not exist!', status.HTTP_404_NOT_FOUND) 
        serializer = TranslateHistorySerializer(queryset)
        return Response(serializer.data)
    
    # Create a new translation with given input information
    def create(self, request):

        if request.POST.get('input_text').strip() == '':
            return Response('Input content cannot be empty!', status.HTTP_400_BAD_REQUEST)
             
        input_text = request.POST.get('input_text')

        # Do google translation
        translation = self.googleTranslate(input_text)

        # Create a record for the translation
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
        # Translate into English
        translation = translate_client.translate(text, target_language='en')
        return translation
