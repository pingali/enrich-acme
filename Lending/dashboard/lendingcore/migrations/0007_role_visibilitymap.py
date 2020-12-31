# Generated by Django 2.2.1 on 2020-10-13 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lendingcore', '0006_auto_20200923_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisibilityMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField(null=True)),
                ('catalog_id', models.IntegerField(null=True)),
                ('role_id', models.IntegerField()),
                ('active', models.BooleanField(default=True, help_text='Enable/Disable', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_visibilitymap_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_visibilitymap_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('desc', models.CharField(max_length=1024, verbose_name='Description')),
                ('notes', models.CharField(blank=True, max_length=1024, verbose_name='Additional Notes')),
                ('active', models.BooleanField(default=True, help_text='Enable/Disable', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_role_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_role_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]