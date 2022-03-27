from django.urls import path
from .views import ObjectViewSet

urlpatterns = [
    path('', ObjectViewSet.as_view())
]
