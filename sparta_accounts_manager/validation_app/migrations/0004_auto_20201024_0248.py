# Generated by Django 3.1.2 on 2020-10-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation_app', '0003_auto_20201024_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlicense',
            name='account_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]