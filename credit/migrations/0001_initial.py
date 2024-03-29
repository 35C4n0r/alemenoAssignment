# Generated by Django 5.0.1 on 2024-01-26 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('monthly_salary', models.FloatField()),
                ('approved_limit', models.IntegerField()),
                ('current_debt', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('loan_amount', models.FloatField()),
                ('tenure', models.IntegerField()),
                ('interest_rate', models.FloatField()),
                ('monthly_repayment', models.FloatField()),
                ('emis_paid_on_time', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.customer')),
            ],
        ),
    ]
