# Generated by Django 2.1.7 on 2019-03-26 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('user', models.IntegerField(blank=True, default=None)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=None)),
            ],
        ),
    ]