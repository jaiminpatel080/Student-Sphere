# Generated by Django 4.2.9 on 2024-02-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSphereApp', '0010_rename_staff_staff_notification_staff_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]