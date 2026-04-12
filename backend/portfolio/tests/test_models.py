"""Unit tests for portfolio models."""

from datetime import date

from django.test import TestCase

from portfolio.models import Certification, Education, Experience, Project, Skill


class ProjectModelTests(TestCase):
    def test_str_returns_title(self):
        project = Project.objects.create(
            title="Alpha",
            description="Desc",
            technologies="Python",
        )
        self.assertEqual(str(project), "Alpha")

    def test_optional_links(self):
        project = Project.objects.create(
            title="Beta",
            description="D",
            technologies="TS",
            Live_link="https://example.com/live",
            Github_link="https://github.com/u/r",
        )
        self.assertEqual(project.Live_link, "https://example.com/live")


class ExperienceModelTests(TestCase):
    def test_str_includes_role_and_company(self):
        exp = Experience.objects.create(
            role="Dev",
            company="Acme",
            start_date=date(2020, 1, 1),
            description="Built things.",
        )
        self.assertEqual(str(exp), "Dev at Acme")


class EducationModelTests(TestCase):
    def test_str_includes_degree_and_institution(self):
        edu = Education.objects.create(
            institution="Uni",
            degree="BSc CS",
            start_date=date(2018, 9, 1),
            end_date=date(2022, 6, 1),
            description="Studied.",
        )
        self.assertEqual(str(edu), "BSc CS from Uni")


class SkillModelTests(TestCase):
    def test_str_returns_name(self):
        skill = Skill.objects.create(name="Django")
        self.assertEqual(str(skill), "Django")


class CertificationModelTests(TestCase):
    def test_str_includes_title_and_org(self):
        cert = Certification.objects.create(
            title="AWS",
            organization="Amazon",
            issue_date=date(2024, 1, 15),
        )
        self.assertIn("AWS", str(cert))
        self.assertIn("Amazon", str(cert))
