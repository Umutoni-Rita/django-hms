# Generated by Django 5.1.2 on 2024-10-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='medical_history',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='patient',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]