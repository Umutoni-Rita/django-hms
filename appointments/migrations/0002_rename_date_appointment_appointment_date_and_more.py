# Generated by Django 5.1.2 on 2024-10-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='appointment_date',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]