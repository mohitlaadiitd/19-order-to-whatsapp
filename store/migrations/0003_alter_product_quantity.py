# Generated by Django 3.2.11 on 2022-02-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220218_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
