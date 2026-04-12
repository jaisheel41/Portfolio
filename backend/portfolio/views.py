from django.http import JsonResponse
from rest_framework import viewsets

from .models import Certification, Education, Experience, Project, Skill
from .serializers import (
    CertificationSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    SkillSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


def api_root(request):
    return JsonResponse({"message": "Portfolio API Root"})
