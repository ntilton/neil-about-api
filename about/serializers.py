from rest_framework import serializers
from .models import Company, Role, Duty, Skill

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['company'] = CompanySerializer(instance.company).data
        rep['skills'] = SkillSerializer(instance.skills.all(), many=True).data
        return rep

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['role'] = RoleSerializer(instance.role).data
        return rep

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


