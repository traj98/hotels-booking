# Generated by Django 2.2.9 on 2020-05-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
