# Generated by Django 5.0 on 2024-01-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_question_topic_alter_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
