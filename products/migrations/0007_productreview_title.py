# Generated by Django 3.1.5 on 2021-02-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productreview_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]