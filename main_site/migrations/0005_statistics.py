# Generated by Django 2.1.1 on 2018-09-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_supporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]