# Generated by Django 3.0.2 on 2022-06-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=800)),
                ('projects', models.CharField(max_length=800)),
            ],
            options={
                'ordering': ['skills'],
            },
        ),
    ]
