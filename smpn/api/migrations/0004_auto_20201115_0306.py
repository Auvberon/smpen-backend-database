# Generated by Django 3.1.1 on 2020-11-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201114_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=144, unique=True),
        ),
    ]