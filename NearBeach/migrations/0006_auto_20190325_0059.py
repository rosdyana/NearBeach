# Generated by Django 2.1.5 on 2019-03-25 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0005_auto_20190325_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_for_change_group_approval',
            name='approval',
            field=models.IntegerField(choices=[(1, 'Waiting'), (2, 'Approved'), (3, 'Rejected'), (4, 'Cancel')], default=1),
        ),
        migrations.AlterField(
            model_name='request_for_change_group_approval',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.group'),
        ),
    ]
