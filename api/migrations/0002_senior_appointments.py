# Generated by Django 5.1.2 on 2024-11-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='senior',
            name='appointments',
            field=models.ManyToManyField(blank=True, related_name='seniors', to='appointments.appointment'),
        ),
    ]
