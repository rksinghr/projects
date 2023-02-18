# Generated by Django 4.1.3 on 2023-01-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_userprofile_userdob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userAddress1',
            new_name='userAddress',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='userAddress2',
            new_name='userDistrict',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='userAddress3',
            new_name='userGender',
        ),
        migrations.AddField(
            model_name='eventtype',
            name='eventDescription',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='eventType',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userRepState',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userState',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='eventName',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
