# Generated by Django 4.0 on 2022-11-09 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0005_alter_crud_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud_student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128),
        ),
    ]
