# Generated by Django 3.2.9 on 2021-12-13 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0005_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceIcon', models.CharField(max_length=50)),
                ('ServiceName', models.CharField(max_length=50)),
                ('ServiceDiscription', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='port.user_profile')),
            ],
        ),
    ]
