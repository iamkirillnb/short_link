# Generated by Django 3.1.3 on 2020-11-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_url', '0003_auto_20201115_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='shortened',
            field=models.CharField(max_length=50, unique=True, verbose_name='short_link'),
        ),
    ]
