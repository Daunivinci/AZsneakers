# Generated by Django 3.0.7 on 2020-06-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200628_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
