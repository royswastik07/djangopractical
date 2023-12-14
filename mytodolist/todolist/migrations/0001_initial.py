# Generated by Django 4.2.7 on 2023-12-01 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('taskid', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('task_title', models.TextField(max_length=255)),
                ('task_description', models.TextField(null=True)),
                ('task_created_on', models.DateTimeField(default=datetime.datetime(2023, 12, 1, 13, 43, 5, 19416))),
                ('task_completed_on', models.DateTimeField()),
            ],
        ),
    ]