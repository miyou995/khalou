# Generated by Django 3.0.7 on 2020-11-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='photo',
            field=models.ImageField(upload_to='produits/'),
        ),
    ]
