# Generated by Django 3.2.6 on 2021-11-09 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_file',
            field=models.FileField(blank=True, upload_to='pdfs'),
        ),
    ]
