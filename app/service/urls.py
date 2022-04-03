from django.urls import path
from app.service.views import FolderViewSet
from app.service.views import FolderDetailViewSet

urlpatterns = [
    path('folder/', FolderViewSet.as_view(), name="folder"),
    path('folder/<uuid:folder_id>', FolderDetailViewSet.as_view(), name="folder_with_id")
]
