# Generated by Django 4.2.1 on 2023-05-29 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
