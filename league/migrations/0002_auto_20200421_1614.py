# Generated by Django 3.0.5 on 2020-04-21 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nflplayer',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='nflplayer',
            name='position',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='nflplayer',
            name='team',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]