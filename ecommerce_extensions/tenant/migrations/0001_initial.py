# Generated by Django 2.2.16 on 2020-10-20 20:47
import collections

import django.db.models.deletion
import jsonfield.encoder
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options_blob', jsonfield.fields.JSONField(
                    default={},
                    dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')},
                    help_text='JSON string containing the extended edunext settings.',
                    load_kwargs={'object_pairs_hook': collections.OrderedDict},
                    verbose_name='Extended Site Options',
                )),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'SiteOptions',
            },
        ),
    ]
