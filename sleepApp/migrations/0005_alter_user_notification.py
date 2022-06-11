# Generated by Django 4.0.4 on 2022-04-25 14:49

from django.db import migrations
import djongo.models.fields
import sleepApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sleepApp', '0004_alter_user_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Notification',
            field=djongo.models.fields.ArrayField(model_container=sleepApp.models.Notification, model_form_class=sleepApp.models.NotificationForm),
        ),
    ]