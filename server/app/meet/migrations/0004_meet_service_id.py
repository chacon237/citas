# Generated by Django 4.1.7 on 2023-03-21 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('meet', '0003_meet_activa_meet_user_id_alter_meet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
    ]
