# Generated by Django 4.2.8 on 2023-12-15 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0004_remove_charity_profile_pic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charity',
            old_name='image1',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='image1',
            new_name='profile_pic',
        ),
    ]