# Generated by Django 3.2.6 on 2022-12-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_answer_question_quiz_quizrepo'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_desc',
            field=models.TextField(default=None),
        ),
    ]