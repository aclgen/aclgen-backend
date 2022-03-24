from django.urls import path
from app.dummy.views import DummyTestViewSet

urlpatterns = [
    path('', DummyTestViewSet.as_view())
]
