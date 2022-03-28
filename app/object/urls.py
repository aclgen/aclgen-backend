from django.urls import path
from .views import ObjectViewSet
from .views import ObjectDetailViewSet

urlpatterns = [
    path('', ObjectViewSet.as_view(), name="object"),
    path('<int:object_id>', ObjectDetailViewSet.as_view(), name="object_with_id")
]
