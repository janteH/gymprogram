# Generated by Django 4.2.13 on 2024-05-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
