# Generated by Django 4.1.7 on 2023-04-06 17:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.DateTimeField(max_length=20)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.service')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='workers.worker')),
            ],
            options={
                'ordering': ['date_created'],
                'abstract': False,
            },
        ),
    ]
