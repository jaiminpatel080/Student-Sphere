# Generated by Django 4.2.9 on 2024-02-24 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSphereApp', '0018_student_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_result',
            old_name='assignment_marks',
            new_name='practical_marks',
        ),
    ]
