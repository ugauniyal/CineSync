# Generated by Django 3.1.7 on 2021-12-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20211222_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary')], max_length=10, null=True),
        ),
    ]
