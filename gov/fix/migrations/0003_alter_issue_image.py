# Generated by Django 3.2.6 on 2021-08-19 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fix', '0002_alter_issue_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
