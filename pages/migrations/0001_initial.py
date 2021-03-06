# Generated by Django 2.1.7 on 2019-03-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('active', 'active'), ('disable', 'disable')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PageLang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=50)),
                ('content', models.TextField(blank=True, default=None)),
                ('lang', models.CharField(max_length=3)),
                ('page_id', models.IntegerField()),
                ('description', models.CharField(blank=True, default=None, max_length=255)),
                ('keywords', models.TextField(blank=True, default=None)),
            ],
        ),
    ]
