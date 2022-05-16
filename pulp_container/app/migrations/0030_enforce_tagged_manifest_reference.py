# Generated by Django 3.2.13 on 2022-05-16 16:13

from django.db import migrations, models
import django.db.models.deletion


def remove_tags_without_manifests(apps, schema_editor):
    Tag = apps.get_model("container", "Tag")
    Tag.objects.filter(tagged_manifest=None).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0029_remove_blob_media_type'),
    ]

    operations = [
        migrations.RunPython(code=remove_tags_without_manifests),
        migrations.AlterField(
            model_name='tag',
            name='tagged_manifest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_manifests', to='container.manifest'),
        ),
    ]
