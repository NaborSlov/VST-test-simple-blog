# Generated by Django 4.2 on 2023-04-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author_name',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
