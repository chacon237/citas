# Generated by Django 4.1.7 on 2023-03-21 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0005_alter_professionals_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='admission_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 17, 30, 3, 566253, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]