# Generated by Django 3.2.8 on 2021-10-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0009_alter_chart_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='album',
            field=models.TextField(blank=True, default='album'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='username',
            field=models.TextField(blank=True, default='username'),
        ),
    ]
