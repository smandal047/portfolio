# Generated by Django 3.1.3 on 2021-04-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_works_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]