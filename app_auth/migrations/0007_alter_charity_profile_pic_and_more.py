# Generated by Django 4.2.8 on 2023-12-16 06:23

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0006_alter_charity_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='charity/profiles/default.jpg', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[900, 500], upload_to='charity/profiles/'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='volunteer/profiles/default.jpg', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[900, 500], upload_to='volunteer/profiles/'),
        ),
    ]