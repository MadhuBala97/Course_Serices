# Generated by Django 3.2.13 on 2022-05-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapplication', '0006_rename_servicet_addservices_stitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phoneno', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
