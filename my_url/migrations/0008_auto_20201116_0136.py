# Generated by Django 3.1.3 on 2020-11-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_url', '0007_auto_20201116_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='flag',
            new_name='change_flag',
        ),
        migrations.AlterField(
            model_name='links',
            name='shortened',
            field=models.CharField(default='YKJlnpjnYA', max_length=50, unique=True, verbose_name='short_link'),
        ),
    ]