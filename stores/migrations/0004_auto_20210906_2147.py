# Generated by Django 3.2.7 on 2021-09-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_alter_stores_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='delivTip',
            field=models.IntegerField(verbose_name='delivTip'),
        ),
        migrations.AlterField(
            model_name='stores',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
    ]