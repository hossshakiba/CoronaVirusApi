# Generated by Django 3.1.4 on 2020-12-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201229_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronavirus',
            name='total_cases',
            field=models.IntegerField(),
        ),
    ]
