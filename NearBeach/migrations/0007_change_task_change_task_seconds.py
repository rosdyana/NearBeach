# Generated by Django 2.2.7 on 2020-02-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0006_object_assignment_requirement_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='change_task',
            name='change_task_seconds',
            field=models.BigIntegerField(default=0),
        ),
    ]
