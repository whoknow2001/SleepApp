# Generated by Django 3.1.12 on 2022-04-25 12:59

from django.db import migrations, models
import sleepApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sleepApp', '0002_user_cmnd_user_email_user_phone_alter_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to=sleepApp.models.upload_to),
        ),
    ]
