# Generated by Django 3.2.6 on 2021-08-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fix', '0007_remove_issue_date_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
