from rest_framework import serializers
from django.conf import settings
from .models import Certification, Education, Experience, Project, Skill


def get_image_url(image_field):
    if not image_field:
        return None
    name = str(image_field)
    if not name:
        return None
    base = getattr(settings, "SUPABASE_STORAGE_PUBLIC_BASE", "").rstrip("/")
    if base:
        return f"{base}/{name}"
    # fallback for local dev
    return image_field.url if hasattr(image_field, 'url') else None


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return get_image_url(obj.image)

    class Meta:
        model = Project
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return get_image_url(obj.logo)

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