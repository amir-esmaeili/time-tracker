# Generated by Django 3.0.8 on 2020-08-05 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0015_auto_20200803_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Projects_name', to='tracker.Project'),
        ),
    ]
