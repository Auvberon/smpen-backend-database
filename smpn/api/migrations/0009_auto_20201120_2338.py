# Generated by Django 3.1.1 on 2020-11-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201118_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logging',
            name='status',
            field=models.BooleanField(choices=[(True, 'In'), (False, 'Out')], null=True),
        ),
    ]