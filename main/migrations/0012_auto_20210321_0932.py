# Generated by Django 3.0.7 on 2021-03-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210320_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file_1',
            field=models.FileField(blank=True, upload_to='fichiers/', verbose_name='Fiche Technique'),
        ),
    ]