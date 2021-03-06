# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-11 05:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lendingcore', '0003_attachment_experiment_experimentrun_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name of Project')),
                ('desc', models.CharField(max_length=1024, verbose_name='Description of Project')),
                ('notes', models.CharField(blank=True, help_text='Instructions to the labelling staff', max_length=1024, verbose_name='Additional Notes')),
                ('dataset', jsonfield.fields.JSONField(help_text='A list of formatted entries that need labelling. See documentation', verbose_name='Dataset')),
                ('labels', jsonfield.fields.JSONField(help_text='A list of formatted labelling choices. See documentation', verbose_name='Labels')),
                ('entries_per_record', models.IntegerField(default=1, verbose_name='Number of Labelling Entries Per Record')),
                ('max_entries_per_labeller', models.IntegerField(default=9999, verbose_name='Max Number of Labelling Entries per Person')),
                ('conflict_rules', jsonfield.fields.JSONField(blank=True, default={}, help_text='A dictionary of rules for conflict conditions', verbose_name='Rules for Conflict Check (If Any)')),
                ('total', models.IntegerField(default=0, help_text='Total Number of Records')),
                ('unlabelled', models.IntegerField(default=0, help_text='Number of Unlabelled Records')),
                ('active', models.BooleanField(default=True)),
                ('expanded', models.BooleanField(default=False, help_text='Whether Records and Entries have been materialized')),
                ('complete', models.IntegerField(default=0, help_text='Number of Labelled Records')),
                ('incomplete', models.IntegerField(default=0, help_text='Number of Records whose Labelling is WIP')),
                ('conflict', models.IntegerField(default=0, help_text='Number of Records whose Labelling is Conflicted')),
                ('conflictc', models.IntegerField(default=0, help_text='Number of Records whose Labelling is Conflicted and completed')),
                ('conflicti', models.IntegerField(default=0, help_text='Number of Records whose Labelling is Conflicted and incomplete')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_annotationmodel_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_annotationmodel_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('annotation_id', models.IntegerField()),
                ('record_id', models.IntegerField()),
                ('record_instance', models.IntegerField(default=0, help_text='Instance of the record')),
                ('external_id', models.IntegerField()),
                ('data', models.CharField(blank=True, default='', max_length=1024)),
                ('desc', models.CharField(blank=True, default='', max_length=1024)),
                ('spec', jsonfield.fields.JSONField(default={})),
                ('choices', jsonfield.fields.JSONField(default={})),
                ('marked', models.BooleanField(default=False)),
                ('visited', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('annotated_at', models.DateTimeField(auto_now=True, null=True)),
                ('annotated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_entrymodel_annotator', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_entrymodel_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_entrymodel_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('annotation_id', models.IntegerField()),
                ('external_id', models.IntegerField()),
                ('data', models.CharField(blank=True, default='', max_length=1024)),
                ('desc', models.CharField(blank=True, default='', max_length=1024)),
                ('spec', jsonfield.fields.JSONField(default={})),
                ('choices', jsonfield.fields.JSONField(default={})),
                ('marked', models.BooleanField(default=False)),
                ('visited', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('entries_completed', models.IntegerField(blank=True, default=0)),
                ('status', models.CharField(blank=True, default='No Conflict', max_length=1024)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_recordmodel_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_recordmodel_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
