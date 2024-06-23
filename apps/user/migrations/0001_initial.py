# Generated by Django 5.0.6 on 2024-06-22 10:10

import apps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('requested_verified', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, default='users/user_default_profile.png', null=True, upload_to=apps.user.models.user_profile_directory_path, verbose_name='Picture')),
                ('banner', models.ImageField(blank=True, default='users/user_default_bg.jpg', null=True, upload_to=apps.user.models.user_banner_directory_path, verbose_name='Banner')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=80, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('profile_info', models.TextField(blank=True, max_length=150, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('pais', models.CharField(blank=True, max_length=255, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('salario', models.IntegerField(blank=True, null=True)),
                ('experiencia', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('comprado', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
