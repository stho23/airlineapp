# Generated by Django 4.1.5 on 2024-01-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight'),
        ),
    ]