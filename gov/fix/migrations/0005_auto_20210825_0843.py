# Generated by Django 3.2.6 on 2021-08-25 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fix', '0004_alter_chat_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='response',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('R', 'Rookie'), ('S', 'Seasoned'), ('P', 'Proficient')], default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('U', 'User'), ('M', 'Moderator')], default='U', max_length=1),
            preserve_default=False,
        ),
    ]
