# Generated by Django 3.0.2 on 2022-06-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0008_auto_20220625_1940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ebooksmodel',
            options={'ordering': ['rollno']},
        ),
        migrations.RemoveField(
            model_name='ebooksmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='ebooksmodel',
            name='rollno',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
