from django.urls import path, include
from rest_framework import routers
from documents import views


app_name = 'documents'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]