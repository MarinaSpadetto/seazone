# Generated by Django 4.2.5 on 2023-09-18 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
