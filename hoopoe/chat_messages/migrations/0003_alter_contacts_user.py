# Generated by Django 4.0.7 on 2025-03-14 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat_messages", "0002_contacts_delete_userconnections"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacts",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
