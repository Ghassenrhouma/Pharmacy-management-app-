# Generated by Django 4.1.5 on 2023-04-24 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0002_alter_patient_table_alter_pharmacist_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacyapp.patient'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.address'),
        ),
    ]