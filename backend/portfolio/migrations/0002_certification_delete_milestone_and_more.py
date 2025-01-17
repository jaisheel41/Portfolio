# Generated by Django 5.0.1 on 2025-01-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('credential_url', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='certifications/')),
            ],
        ),
        migrations.DeleteModel(
            name='Milestone',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='link',
            new_name='Github_link',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='level',
        ),
        migrations.AddField(
            model_name='project',
            name='Linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
