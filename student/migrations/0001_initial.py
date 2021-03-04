# Generated by Django 3.1.4 on 2021-03-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('roll_no', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=60)),
                ('marks_maths', models.PositiveIntegerField()),
                ('marks_physics', models.PositiveIntegerField()),
                ('marks_chemistry', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('percentage', models.FloatField()),
            ],
        ),
    ]