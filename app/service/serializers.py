from rest_framework import serializers
from app.service.models import Folder


class SubFolderSerializer(serializers.HyperlinkedModelSerializer):
    #parent_folder = serializers.PrimaryKeyRelatedField(queryset=Folder.objects.all(), source="id")

    class Meta:
        model = Folder
        fields = [
            "id",
            "name",
            #"parent_folder",
            "created_on",
            "modified_on",
        ]


class FolderSerializer(serializers.ModelSerializer):
    children = SubFolderSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = [
            "id",
            "name",
            "parent_folder",
            "children",
            "created_on",
            "modified_on",
        ]
