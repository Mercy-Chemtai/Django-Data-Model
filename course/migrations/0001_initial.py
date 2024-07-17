# Generated by Django 5.0.7 on 2024-07-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(max_length=10)),
                ('students_taking', models.PositiveSmallIntegerField()),
                ('course_Id', models.PositiveSmallIntegerField()),
                ('class_teacher', models.CharField(max_length=10)),
                ('school_name', models.CharField(max_length=10)),
                ('course_passmark', models.PositiveSmallIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('class_time', models.PositiveSmallIntegerField()),
                ('room_number', models.PositiveSmallIntegerField()),
                ('Academic_year', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
