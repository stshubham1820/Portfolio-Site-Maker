# Generated by Django 3.2.9 on 2021-12-30 08:10

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0010_auto_20211230_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_about',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True),
        ),
    ]