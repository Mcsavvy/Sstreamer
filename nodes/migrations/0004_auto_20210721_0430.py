# Generated by Django 3.2.5 on 2021-07-21 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0001_initial'),
        ('nodes', '0003_auto_20210720_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='dp',
        ),
        migrations.AlterField(
            model_name='node',
            name='instagram',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node', to='socials.instagram'),
        ),
    ]
