# Generated by Django 3.0.3 on 2023-11-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=256)),
                ('blog_content', models.CharField(max_length=2000)),
                ('blog_author', models.CharField(max_length=256)),
                ('blog_creation_date', models.DateField()),
            ],
        ),
    ]
