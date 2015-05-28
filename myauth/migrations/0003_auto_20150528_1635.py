# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_auto_20150528_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='tag_line',
            new_name='tagline',
        ),
    ]
