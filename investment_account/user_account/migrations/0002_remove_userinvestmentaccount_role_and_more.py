# Generated by Django 4.2.16 on 2024-09-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinvestmentaccount',
            name='role',
        ),
        migrations.AddField(
            model_name='userinvestmentaccount',
            name='can_create',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinvestmentaccount',
            name='can_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinvestmentaccount',
            name='can_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinvestmentaccount',
            name='can_view',
            field=models.BooleanField(default=False),
        ),
    ]
