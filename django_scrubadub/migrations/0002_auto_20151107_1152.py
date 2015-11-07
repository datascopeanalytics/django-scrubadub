# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import scrubadub


def add_scrubadub_filth_types(apps, schema_editor):
    FilthType = apps.get_model("django_scrubadub", "FilthType")

    for name, detector_cls in scrubadub.detectors.types.iteritems():
        filth_type, created = FilthType.objects.get_or_create(
            name=name,
            detector_cls=detector_cls.__module__ + '.' + detector_cls.__name__,
        )
        if created:
            print "'%s' filth type created" % name


class Migration(migrations.Migration):

    dependencies = [
        ('django_scrubadub', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_scrubadub_filth_types)
    ]
