# Generated by Django 2.1.1 on 2018-09-12 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webansi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='args',
            old_name='arge_text',
            new_name='args_text',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='model_name',
            new_name='module_name',
        ),
    ]
