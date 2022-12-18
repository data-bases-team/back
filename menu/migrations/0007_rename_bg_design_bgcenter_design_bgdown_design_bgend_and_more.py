# Generated by Django 4.1.3 on 2022-12-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_design_cafename_alter_design_fontcolor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='bg',
            new_name='bgcenter',
        ),
        migrations.AddField(
            model_name='design',
            name='bgdown',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='design',
            name='bgend',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='design',
            name='bgheader',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='design',
            name='bgpage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='design',
            name='bgup',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
