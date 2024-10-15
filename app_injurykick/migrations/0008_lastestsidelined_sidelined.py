# Generated by Django 5.1.1 on 2024-10-15 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_injurykick', '0007_alter_news_api_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastestSidelined',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('player_name', models.CharField(max_length=255)),
                ('player_link', models.URLField()),
                ('injury_type', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.CharField(blank=True, max_length=50, null=True)),
                ('end_date', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('injured', 'Injured'), ('recovered', 'Recovered')], default='injured', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sidelined',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_injurykick.player')),
            ],
        ),
    ]
