# Generated by Django 3.2 on 2022-03-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rasm',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]