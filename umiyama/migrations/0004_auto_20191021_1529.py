# Generated by Django 2.2.6 on 2019-10-21 09:59

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('umiyama', '0003_masterpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmaapage',
            name='maa_description',
            field=wagtail.core.fields.RichTextField(help_text='Fill the field', null=True),
        ),
    ]