# Generated by Django 3.1.1 on 2020-11-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201120_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logging',
            name='id',
        ),
        migrations.AlterField(
            model_name='logging',
            name='logical_uid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]