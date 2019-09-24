# Generated by Django 2.1.1 on 2018-09-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_auto_20180905_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('site_link', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='supporter_photo/')),
            ],
        ),
    ]
