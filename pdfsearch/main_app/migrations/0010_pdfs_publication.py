# Generated by Django 5.0 on 2023-12-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_pdfs_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfs',
            name='publication',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
