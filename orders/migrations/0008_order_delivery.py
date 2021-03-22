# Generated by Django 3.0.7 on 2021-03-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210311_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.DecimalField(decimal_places=2, default=1.1, max_digits=10, verbose_name='Coût de Livraison'),
            preserve_default=False,
        ),
    ]