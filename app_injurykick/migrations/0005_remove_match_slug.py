# Generated by Django 5.1.1 on 2024-10-07 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_injurykick', '0004_remove_league_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='slug',
        ),
    ]