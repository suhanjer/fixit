# Generated by Django 3.2.6 on 2021-08-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]