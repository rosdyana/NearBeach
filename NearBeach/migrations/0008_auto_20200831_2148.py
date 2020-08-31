# Generated by Django 2.1.7 on 2020-08-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0007_object_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_history',
            name='change_user',
        ),
        migrations.RemoveField(
            model_name='project_history',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='project_history',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='task_history',
            name='change_user',
        ),
        migrations.RemoveField(
            model_name='task_history',
            name='task_id',
        ),
        migrations.RemoveField(
            model_name='task_history',
            name='user_id',
        ),
        migrations.AddField(
            model_name='object_note',
            name='object_note',
            field=models.TextField(default='HELLO WORLD'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='object_note',
            table='object_notes',
        ),
        migrations.DeleteModel(
            name='project_history',
        ),
        migrations.DeleteModel(
            name='task_history',
        ),
    ]
