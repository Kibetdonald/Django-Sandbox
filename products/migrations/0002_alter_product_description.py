# Generated by Django 3.2.7 on 2022-01-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
