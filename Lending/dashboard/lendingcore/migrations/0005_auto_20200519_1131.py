# Generated by Django 2.2 on 2020-05-19 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lendingcore', '0004_annotationmodel_entrymodel_recordmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_annotationmodel_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='annotationmodel',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_annotationmodel_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_attachment_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='file_contents',
            field=models.BinaryField(editable=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_attachment_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_catalog_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_catalog_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='column',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_column_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='column',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_column_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_comment_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_comment_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_datasource_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_datasource_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entrymodel',
            name='annotated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_entrymodel_annotator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entrymodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_entrymodel_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entrymodel',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_entrymodel_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_experiment_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_experiment_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experimentrun',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_experimentrun_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experimentrun',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_experimentrun_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feature',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_feature_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feature',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_feature_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_featurerequest_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_featurerequest_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recordmodel',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_recordmodel_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recordmodel',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lendingcore_recordmodel_modifier', to=settings.AUTH_USER_MODEL),
        ),
    ]