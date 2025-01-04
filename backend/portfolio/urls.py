from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Set up a router and register our viewsets
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'certifications', views.CertificationViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
