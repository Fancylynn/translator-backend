from django.urls import path
from rest_framework import routers
from .views import TranslatorViewSet

router = routers.DefaultRouter()
router.register('translate', TranslatorViewSet, base_name='translate')
urlpatterns = router.urls