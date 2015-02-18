# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_venue', models.CharField(max_length=120, null=True)),
                ('event_title', models.CharField(max_length=120, null=True)),
                ('main_event_addy', models.CharField(max_length=120, null=True)),
                ('secondary_event_addy', models.CharField(max_length=120, null=True)),
                ('event_addy_city', models.CharField(max_length=90, null=True)),
                ('event_addy_zip', models.CharField(max_length=5, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VenueRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venue_name', models.CharField(max_length=120)),
                ('mng_first_name', models.CharField(max_length=120)),
                ('mng_last_name', models.CharField(max_length=120)),
                ('event_url', models.URLField()),
                ('venue_phone', models.CharField(max_length=10, null=True)),
                ('main_venue_addy', models.CharField(max_length=120, null=True)),
                ('secondary_venue_addy', models.CharField(max_length=120, null=True)),
                ('venue_city', models.CharField(max_length=90, null=True)),
                ('venue_zip', models.CharField(max_length=5, null=True)),
                ('venue_fb', models.CharField(max_length=120, null=True, blank=True)),
                ('venue_twitter', models.CharField(max_length=120, null=True, blank=True)),
                ('venue_yelp', models.CharField(max_length=120, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='event_category',
            field=models.ForeignKey(to='signups.EventCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='first_name',
            field=models.CharField(default='', max_length=120, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='last_name',
            field=models.CharField(default='', max_length=120, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(default='', max_length=120, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='last_name',
            field=models.CharField(default='', max_length=120, blank=True),
            preserve_default=False,
        ),
    ]
