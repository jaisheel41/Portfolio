"""Integration tests for REST API endpoints."""

from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from portfolio.models import Certification, Project, Skill


class ProjectAPITests(APITestCase):
    def test_list_projects_empty(self):
        url = reverse("project-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_create_and_list_project(self):
        url = reverse("project-list")
        payload = {
            "title": "App",
            "description": "A project",
            "technologies": "Django, React",
        }
        create = self.client.post(url, payload, format="json")
        self.assertEqual(create.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)

        list_resp = self.client.get(url)
        self.assertEqual(list_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list_resp.data), 1)
        self.assertEqual(list_resp.data[0]["title"], "App")

    def test_retrieve_project(self):
        project = Project.objects.create(
            title="X",
            description="Y",
            technologies="Z",
        )
        url = reverse("project-detail", kwargs={"pk": project.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "X")


class SkillAPITests(APITestCase):
    def test_create_skill(self):
        url = reverse("skill-list")
        response = self.client.post(url, {"name": "TypeScript"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Skill.objects.get().name, "TypeScript")


class CertificationAPITests(APITestCase):
    def test_create_certification(self):
        url = reverse("certification-list")
        payload = {
            "title": "CKA",
            "organization": "CNCF",
            "issue_date": str(date(2023, 5, 1)),
            "description": "",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Certification.objects.count(), 1)


class SiteRootTests(APITestCase):
    def test_welcome_message(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json().get("message"),
            "Welcome to the Portfolio API",
        )
