# Generated by Django 2.1.5 on 2021-07-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20171219_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='blank_profile/None.jpg', upload_to='profile_images', verbose_name='Profile Picture'),
        ),
    ]