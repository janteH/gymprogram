# Generated by Django 4.2.13 on 2024-05-27 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0002_move_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True)),
                ('move', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gymapp.move')),
            ],
        ),
    ]
