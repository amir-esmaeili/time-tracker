# Generated by Django 3.0.8 on 2020-07-19 19:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20200720_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]