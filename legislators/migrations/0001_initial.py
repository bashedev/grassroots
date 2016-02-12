# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legislator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bioguide_id', models.CharField(max_length=7)),
                ('birthday', models.CharField(max_length=10)),
                ('chamber', models.CharField(choices=[('H', 'House'), ('S', 'Senate')], max_length=2)),
                ('contact_form', models.URLField()),
                ('crp_id', models.CharField(max_length=10)),
                ('district', models.IntegerField()),
                ('facebook_id', models.CharField(max_length=30)),
                ('fax', models.IntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('govtrack_id', models.CharField(max_length=10)),
                ('in_office', models.BooleanField()),
                ('last_name', models.CharField(max_length=30)),
                ('leadership_role', models.CharField(max_length=254)),
                ('middle_name', models.CharField(max_length=20)),
                ('name_suffix', models.CharField(max_length=15)),
                ('nickname', models.CharField(max_length=15)),
                ('oc_email', models.EmailField(max_length=254)),
                ('ocd_id', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=50)),
                ('party', models.CharField(choices=[('R', 'Republican'), ('D', 'Democrat'), ('I', 'Independent'), ('G', 'Green')], max_length=1)),
                ('phone', models.CharField(max_length=14)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MH', 'Marshall Islands'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('FM', 'Micronesia'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Marianas'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('state_name', models.CharField(max_length=20)),
                ('term_end', models.DateField()),
                ('term_start', models.DateField()),
                ('thomas_id', models.IntegerField()),
                ('title', models.CharField(max_length=15)),
                ('twitter_id', models.CharField(max_length=20)),
            ],
        ),
    ]