# Generated by Django 3.2.6 on 2021-08-23 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fix', '0003_alter_issue_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation', to='fix.issue'),
        ),
    ]
