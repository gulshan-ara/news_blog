# Generated by Django 3.0.3 on 2023-11-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20231124_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='blog_image_primary',
            field=models.ImageField(upload_to='img/%y'),
        ),
    ]