from django.conf.urls import include
from django.urls import path
from .views import LemmasAPIView

urlpatterns = [
    path('api/v1/getalllemmas', LemmasAPIView.as_view())
]
