from django.db import models

# Create your models here.
class TranslateHistory(models.Model):
    input_text = models.TextField()
    language = models.CharField(max_language=50)
    translation = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)