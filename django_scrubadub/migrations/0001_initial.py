# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Filth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beg', models.IntegerField()),
                ('end', models.IntegerField()),
                ('text', models.CharField(max_length=255)),
                ('document', models.ForeignKey(to='django_scrubadub.Document')),
            ],
        ),
        migrations.CreateModel(
            name='FilthType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('detector_cls', models.CharField(max_length=255)),
                ('parameters', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='filth',
            name='type',
            field=models.ForeignKey(to='django_scrubadub.FilthType'),
        ),
    ]
