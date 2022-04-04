from django.urls import path
from app.service.views import FolderViewSet, ServiceViewSet, ServiceViewSetNew
from app.service.views import FolderDetailViewSet
from rest_framework import routers
from app.service import views

urlpatterns = [
    path('folder/', FolderViewSet.as_view(), name="folder"),
    path('folder/<uuid:folder_id>', FolderDetailViewSet.as_view(), name="folder_with_id"),
    path('service/', ServiceViewSetNew.as_view({"get": "list", "post": "create"}), name="service"),
]
