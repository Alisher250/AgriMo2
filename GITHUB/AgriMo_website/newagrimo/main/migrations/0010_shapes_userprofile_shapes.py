# Generated by Django 4.1.7 on 2023-07-11 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_rename_geolocation_userprofile_geolocation1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shapes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='shapes',
            field=models.ManyToManyField(blank=True, to='main.shapes'),
        ),
    ]
