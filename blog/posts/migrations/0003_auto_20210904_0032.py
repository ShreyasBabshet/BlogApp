# Generated by Django 3.1.3 on 2021-09-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(default='', upload_to='filepath'),
        ),
    ]
