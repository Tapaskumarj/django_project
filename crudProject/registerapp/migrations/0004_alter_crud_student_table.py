# Generated by Django 4.0 on 2022-11-07 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0003_alter_crud_student_gender_alter_crud_student_state'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='crud_student',
            table='student',
        ),
    ]
