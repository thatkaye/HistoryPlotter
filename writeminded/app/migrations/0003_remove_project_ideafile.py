# Generated by Django 4.1.2 on 2022-12-13 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_relations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ideafile',
        ),
    ]