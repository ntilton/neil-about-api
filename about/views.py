from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Role, Duty, Skill
from .serializers import CompanySerializer,RoleSerializer, DutySerializer, SkillSerializer

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-dateStart')
    serializer_class = CompanySerializer

class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('-dateStart')
    serializer_class = RoleSerializer

class DutyView(viewsets.ModelViewSet):
    queryset = Duty.objects.all().order_by('id')
    serializer_class = DutySerializer

class SkillView(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('name')
    serializer_class = SkillSerializer
