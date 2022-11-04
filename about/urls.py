from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import CompanyView, RoleView, DutyView, SkillView

router = routers.DefaultRouter()
router.register(r'companies', CompanyView)
router.register(r'roles', RoleView)
router.register(r'duties', DutyView)
router.register(r'skills', SkillView)


urlpatterns = [
    path('', include(router.urls)),
]