from django.urls import path
from app.rules_old.views.ruleset import RuleSetViewSet

urlpatterns = [
    path('rulesets/', RuleSetViewSet.as_view(), name="ruleset")
]
