# Generated by Django 2.1.1 on 2018-09-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_auto_20180905_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='application_end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='application_start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(null=True),
        ),
    ]