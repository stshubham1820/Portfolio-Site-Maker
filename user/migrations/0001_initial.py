# Generated by Django 3.2.9 on 2021-12-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
