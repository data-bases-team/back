# Generated by Django 4.1.3 on 2022-12-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_rename_bg_design_bgcenter_design_bgdown_design_bgend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='headertxt',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
