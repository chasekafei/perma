# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-04 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

def copy_keys(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return
    cursor = schema_editor.connection.cursor()
    try:
        cursor.execute("INSERT INTO perma_apikey SELECT * FROM tastypie_apikey")
    except django.db.utils.ProgrammingError:
        pass  # old tastypie api_key table doesn't exist for this deployment

class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0022_auto_20170320_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, db_index=True, default=b'', max_length=128)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_key', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(copy_keys),
    ]

