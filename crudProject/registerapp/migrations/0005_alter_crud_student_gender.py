# Generated by Django 4.0 on 2022-11-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0004_alter_crud_student_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud_student',
            name='gender',
            field=models.CharField(max_length=128),
        ),
    ]
