# Generated by Django 3.0.5 on 2020-04-28 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_auto_20200428_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastseason',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='league.Owner'),
        ),
    ]
