# Generated by Django 3.1.5 on 2021-02-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_productreview_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='title',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]