# Generated by Django 2.2.6 on 2019-10-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_navigationimage_navimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navigationimage',
            old_name='image',
            new_name='nvimage',
        ),
    ]