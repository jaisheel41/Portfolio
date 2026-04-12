from rest_framework import serializers
from django.conf import settings
from .models import Certification, Education, Experience, Project, Skill


def build_media_url(field_value):
    if not field_value:
        return None
    name = str(field_value)
    if not name:
        return None
    base = getattr(settings, "SUPABASE_STORAGE_PUBLIC_BASE", "").rstrip("/")
    if base:
        return f"{base}/{name}"
    return field_value.url if hasattr(field_value, "url") else None


class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        return build_media_url(obj.image)

    class Meta:
        model = Project
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()

    def get_logo_url(self, obj):
        return build_media_url(obj.logo)

    class Meta:
        model = Certification
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
