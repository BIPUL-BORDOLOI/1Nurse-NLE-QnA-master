# Generated by Django 5.0 on 2024-01-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_question_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
