# Generated by Django 2.2.7 on 2019-12-29 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactive_english_dictionary', '0002_auto_20191229_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionaryquery',
            old_name='result1',
            new_name='result',
        ),
    ]
