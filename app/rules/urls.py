from django.urls import path
from app.rules.views import RuleSetViewSet, RuleSetDetailViewSet, RuleViewSet

urlpatterns = [
    path('ruleset/', RuleSetViewSet.as_view(), name="ruleset"),
    path('ruleset/<uuid:ruleset_id>', RuleSetDetailViewSet.as_view(), name="ruleset_by_id"),
    path('rule/', RuleViewSet.as_view(), name="rule")
]