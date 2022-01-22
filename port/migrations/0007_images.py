# Generated by Django 3.2.9 on 2021-12-15 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0006_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='port.user_profile')),
            ],
        ),
    ]