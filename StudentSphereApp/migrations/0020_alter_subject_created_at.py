# Generated by Django 4.2.9 on 2024-02-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSphereApp', '0019_rename_assignment_marks_student_result_practical_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]