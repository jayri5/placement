# Generated by Django 3.0.2 on 2022-06-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0006_projects_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='rollno',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='rollno',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]