# Generated by Django 3.2.9 on 2021-12-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0009_auto_20211230_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_about',
            name='Awards',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_about',
            name='Hrs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_about',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_about',
            name='clients',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_about',
            name='project',
            field=models.IntegerField(null=True),
        ),
    ]
