# Generated by Django 3.0.3 on 2023-11-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_auto_20231124_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='blog_content',
            field=models.TextField(),
        ),
    ]
