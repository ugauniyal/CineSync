# Generated by Django 3.1.7 on 2021-12-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_moviestatus_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='Not Specified', max_length=300),
        ),
    ]
