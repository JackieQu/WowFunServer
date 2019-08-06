# Generated by Django 2.2.3 on 2019-08-06 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet', to=settings.AUTH_USER_MODEL),
        ),
    ]