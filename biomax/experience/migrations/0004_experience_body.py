# Generated by Django 4.0.1 on 2022-01-28 15:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_experience_created_alter_experience_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
