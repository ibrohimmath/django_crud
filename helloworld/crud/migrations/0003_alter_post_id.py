# Generated by Django 5.1.3 on 2024-12-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
