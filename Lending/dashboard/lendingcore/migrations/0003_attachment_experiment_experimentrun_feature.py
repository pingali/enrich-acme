# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-11 04:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enrichapp.dashboard.marketplace.modellib


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lendingcore', '0002_auto_20190814_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('desc', models.CharField(max_length=1024, verbose_name='Description')),
                ('active', models.BooleanField(default=True, help_text='Enable/Disable', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('catalog_id', models.IntegerField()),
                ('file_contents', models.BinaryField()),
                ('file_type', models.CharField(max_length=10, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_attachment_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_attachment_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Enable/Disable', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('server', models.CharField(max_length=256, verbose_name='Name of backend server')),
                ('nature', models.CharField(choices=[('mlflow', 'mlflow'), ('modeldb', 'modeldb'), ('custom', 'custom')], max_length=32, verbose_name='Nature of backend - mlflow/modeldb/custom')),
                ('experiment_id', models.CharField(max_length=16, verbose_name='Experiment ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('artifact_location', models.CharField(blank=True, max_length=256, null=True)),
                ('lifecycle_stage', models.CharField(blank=True, choices=[('active', 'active'), ('deleted', 'deleted')], default='active', max_length=32, null=True)),
                ('extra', models.TextField(default='{}', validators=[enrichapp.dashboard.marketplace.modellib.validate_dict], verbose_name='Any extra attributes')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_experiment_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_experiment_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExperimentRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Enable/Disable', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('run_uuid', models.CharField(max_length=32, verbose_name='Unique ID for the run')),
                ('name', models.CharField(blank=True, default='unknown', max_length=250, verbose_name='Name of the run if any')),
                ('source_type', models.CharField(default='LOCAL', max_length=20, verbose_name='What the type of the training source (default: LOCAL)')),
                ('source_name', models.CharField(max_length=500, verbose_name='Name of the source of model, if any')),
                ('entry_point_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Entry-point name that launched the run')),
                ('user_id', models.CharField(max_length=256, verbose_name='Name of the user')),
                ('status', models.CharField(choices=[('RUNNING', 'RUNNING'), ('SCHEDULED', 'SCHEDULED'), ('FINISHED', 'FINISHED'), ('FAILED', 'FAILED')], default='SCHEDULED', max_length=20)),
                ('start_time', models.BigIntegerField()),
                ('end_time', models.BigIntegerField()),
                ('source_version', models.CharField(max_length=50, verbose_name='GIT commit of Code')),
                ('lifecycle_stage', models.CharField(choices=[('active', 'active'), ('deleted', 'deleted')], default='active', max_length=20)),
                ('artifact_uri', models.CharField(max_length=200, verbose_name='Location of the artifacts')),
                ('server', models.CharField(max_length=256, verbose_name='Name of backend server')),
                ('experiment_id', models.CharField(max_length=16, verbose_name='Experiment ID')),
                ('extra', models.TextField(default='{}', validators=[enrichapp.dashboard.marketplace.modellib.validate_dict], verbose_name='Any extra attributes')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_experimentrun_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_experimentrun_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Enable/Disable', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('namespace', models.CharField(max_length=32, verbose_name='Namespace')),
                ('name', models.CharField(max_length=32, verbose_name='Name of the feature')),
                ('description', models.CharField(max_length=1024, verbose_name='Description of the feature')),
                ('status', models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('DEFAULT', 'DEFAULT'), ('PRODUCTION', 'PRODUCTION'), ('EXPERIMENTAL', 'EXPERIMENTAL'), ('DEPRECATED', 'DEPRECATED'), ('DISCONTINUED', 'DISCONTINUED'), ('OTHER', 'OTHER')], default='DEFAULT', max_length=32, verbose_name='Status of Feature')),
                ('owner', models.CharField(max_length=32, verbose_name='Name of individual/team owning this feature')),
                ('priority', models.CharField(choices=[('p0', 'p0'), ('p1', 'p1'), ('p2', 'p2'), ('p3', 'p3'), ('p4', 'p4'), ('px', 'px')], default='px', max_length=16, verbose_name='Priority of the feature')),
                ('details', models.TextField(default='[]', help_text='Examples include statistics, sample etc', validators=[enrichapp.dashboard.marketplace.modellib.validate_details], verbose_name='Feature Details')),
                ('process', models.TextField(default='{}', help_text='Pipeline/process generating the feature including server', validators=[enrichapp.dashboard.marketplace.modellib.validate_process], verbose_name='Pipeline')),
                ('generator_name', models.CharField(max_length=32, verbose_name='Name of the generator process')),
                ('generator_runid', models.CharField(max_length=32, verbose_name='Name of run of the generator')),
                ('generated_at', models.DateTimeField(help_text='Time when the feature was generated', verbose_name='Generated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_feature_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lendingcore_feature_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
