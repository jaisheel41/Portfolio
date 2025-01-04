from rest_framework import serializers
from .models import Project, Experience, Education, Skill, Certification

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ['id', 'title', 'description', 'technologies', 'link', 'image']
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'
