from django.urls import path
from app.api.views import repo, device, object, service, rule, folder

# Views

repo_list = repo.RepositoryViewSet.as_view({"get": "list", "post": "create"})
repo_detail = repo.RepositoryViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})
repo_full = repo.RepositoryViewSet.as_view({"get": "retrieve_full"})

device_list = device.DeviceViewSet.as_view({"get": "list", "post": "create"})
device_detail = device.DeviceViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})

object_list = object.ObjectViewSet.as_view({"get": "list", "post": "create", "put": "update"})
object_detail = object.ObjectViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})

service_list = service.ServiceViewSet.as_view({"get": "list", "post": "create", "put": "update"})
service_detail = service.ServiceViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})

rule_list = rule.RuleViewSet.as_view({"get": "list", "post": "create"})
rule_detail = rule.RuleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})

folder_list = folder.DeviceFolderViewSet.as_view({"get": "list", "post": "create"})
folder_detail = folder.DeviceFolderViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})

urlpatterns = [
    # Repos
    path("repo/", repo_list, name="repositories"),
    path("repo/<uuid:id>/", repo_detail, name="repository"),
    path("repo/<uuid:id>/full", repo_full, name="repository_full"),

    # Devices
    path("repo/<uuid:repo_id>/device/", device_list, name="devices"),
    path("repo/<uuid:repo_id>/device/<uuid:dev_id>/", device_detail, name="device"),

    # Device Rules
    path("repo/<uuid:repo_id>/device/<uuid:dev_id>/rule/", rule_list, name="rules"),
    path("repo/<uuid:repo_id>/device/<uuid:dev_id>/rule/<uuid:rule_id>/", rule_detail, name="rule"),

    # Folders
    path("repo/<uuid:repo_id>/device/<uuid:dev_id>/folder/", folder_list, name="device_folders"),
    path("repo/<uuid:repo_id>/device/<uuid:dev_id>/folder/<uuid:folder_id>/", folder_detail, name="device_folder"),

    # Objects
    path("repo/<uuid:repo_id>/object/", object_list, name="objects"),
    path("repo/<uuid:repo_id>/object/<uuid:object_id>/", object_detail, name="object"),

    # Services
    path("repo/<uuid:repo_id>/service/", service_list, name="services"),
    path("repo/<uuid:repo_id>/service/<uuid:service_id>/", service_detail, name="service"),
]
