# Generated by Django 5.0.1 on 2024-02-12 10:34

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpage_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='category',
            field=wagtail.fields.StreamField([('category', wagtail.blocks.ChoiceBlock(choices=[('HappyFox Help Desk', 'HappyFox Help Desk'), ('HappyFox Service Desk', 'HappyFox Service Desk'), ('HappyFox BI', 'HappyFox BI'), ('HappyFox ChatBot', 'HappyFox ChatBot'), ('Miscellaneous', 'Miscellaneous')]))], blank=True),
        ),
    ]