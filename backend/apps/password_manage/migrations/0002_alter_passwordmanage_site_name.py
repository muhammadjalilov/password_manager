# Generated by Django 5.1.3 on 2024-11-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordmanage',
            name='site_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Site Name'),
        ),
    ]
