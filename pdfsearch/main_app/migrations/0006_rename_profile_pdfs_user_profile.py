# Generated by Django 5.0 on 2023-12-15 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_pdfs_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdfs',
            old_name='profile',
            new_name='user_profile',
        ),
    ]
