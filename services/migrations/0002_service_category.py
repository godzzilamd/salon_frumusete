# Generated by Django 4.1.7 on 2023-04-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(default='common', max_length=20),
        ),
    ]
