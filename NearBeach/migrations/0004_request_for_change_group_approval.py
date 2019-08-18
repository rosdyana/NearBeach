# Generated by Django 2.1.5 on 2019-03-25 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0003_request_for_change_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='request_for_change_group_approval',
            fields=[
                ('rfc_group_approval_id', models.AutoField(primary_key=True, serialize=False)),
                ('approval', models.IntegerField(choices=[(1, 'Waiting'), (2, 'Approved'), (3, 'Rejected')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_for_change_group_approval_change_user', to=settings.AUTH_USER_MODEL)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.group')),
                ('rfc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.request_for_change')),
            ],
            options={
                'db_table': 'request_for_change_group_approval',
            },
        ),
    ]