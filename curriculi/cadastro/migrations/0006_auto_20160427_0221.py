# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20160419_2357'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scrip',
            new_name='Script',
        ),
    ]
