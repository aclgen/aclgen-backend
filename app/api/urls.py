from django.urls import path
from rest_framework import routers
from app.api.views import repo, device, ruleset, object, service, rule

# Views

repo_list = repo.RepositoryViewSet.as_view({"get": "list", "post": "create"})
repo_detail = repo.RepositoryViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})

device_list = device.DeviceViewSet.as_view({"get": "list", "post": "create"})
device_detail = device.DeviceViewSet.as_view({"get": "retrieve", "delete": "destroy"})

ruleset_list = ruleset.RuleSetViewSet.as_view({"get": "list", "post": "create"})
ruleset_detail = ruleset.RuleSetViewSet.as_view({"get": "retrieve", "delete": "destroy"})

object_list = object.ObjectViewSet.as_view({"get": "list", "post": "create"})
object_detail = object.ObjectViewSet.as_view({"get": "retrieve", "delete": "destroy"})

service_list = service.ServiceViewSet.as_view({"get": "list", "post": "create"})
service_detail = service.ServiceViewSet.as_view({"get": "retrieve", "delete": "destroy"})

rule_list = rule.RuleViewSet.as_view({"get": "list", "post": "create"})
rule_detail = rule.RuleViewSet.as_view({"get": "retrieve", "delete": "destroy"})

urlpatterns = [
    # Repos
    path("repo/", repo_list, name="repositories"),
    path("repo/<uuid:id>/", repo_detail, name="repository"),

    # Devices
    path("repo/<uuid:repo_id>/workspace/device/", device_list, name="devices"),
    path("repo/<uuid:repo_id>/workspace/device/<uuid:dev_id>/", device_detail, name="device"),

    # Rules
    path("repo/<uuid:repo_id>/workspace/device/<uuid:dev_id>/ruleset/", ruleset_list, name="rulesets"),
    path("repo/<uuid:repo_id>/workspace/device/<uuid:dev_id>/ruleset/<uuid:ruleset_id>/", ruleset_detail, name="ruleset"),

    path("repo/<uuid:repo_id>/workspace/device/<uuid:dev_id>/ruleset/<uuid:ruleset_id>/rule/", rule_list, name="rules"),
    path("repo/<uuid:repo_id>/workspace/device/<uuid:dev_id>/ruleset/<uuid:ruleset_id>/rule/<uuid:rule_id>/",
         rule_detail, name="rule"),

    # Objects
    path("repo/<uuid:repo_id>/object/", object_list, name="objects"),
    path("repo/<uuid:repo_id>/object/<uuid:object_id>/", object_detail, name="object"),

    # Services
    path("repo/<uuid:repo_id>/service/", service_list, name="services"),
    path("repo/<uuid:repo_id>/service/<uuid:service_id>/", service_detail, name="service"),
]