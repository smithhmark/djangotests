# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
