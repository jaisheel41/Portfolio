from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    Live_link = models.URLField(blank=True, null=True)
    Github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Certification(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    description = models.TextField(blank=True)
    credential_url = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='certifications/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.organization}"
