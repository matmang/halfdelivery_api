# Generated by Django 3.2.7 on 2021-09-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_remove_stores_what'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='minprice',
            field=models.CharField(max_length=255, verbose_name='minprice'),
        ),
    ]
