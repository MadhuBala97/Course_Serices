# Generated by Django 3.2.13 on 2022-05-10 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapplication', '0004_addservices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addservices',
            old_name='servicee',
            new_name='servicet',
        ),
    ]