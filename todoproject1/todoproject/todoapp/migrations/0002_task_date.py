# Generated by Django 4.2.4 on 2023-08-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-4-26'),
            preserve_default=False,
        ),
    ]
