# Generated by Django 5.1.1 on 2024-10-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_injurykick', '0006_category_news_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='api_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
