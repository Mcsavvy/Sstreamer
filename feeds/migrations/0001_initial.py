# Generated by Django 3.2.5 on 2021-07-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('thumbnail', models.URLField()),
                ('channel', models.CharField(max_length=100)),
                ('channelId', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]