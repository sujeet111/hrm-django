# Generated by Django 3.2.13 on 2022-12-29 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('ph_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Approved_status', models.BooleanField(null=True)),
                ('Expense_category', models.CharField(choices=[('Travel and Accommodation', 'Travel and Accommodation'), ('Parts Replaced', 'Parts Replaced')], max_length=30)),
                ('Visit_purpose', models.CharField(choices=[('Sales', 'Sales'), ('Installtion', 'Installtion'), ('Customer Support', 'Customer Support'), ('Site Visit', 'Site Visit'), ('Preventive Maintenance', 'Preventive Maintenance')], max_length=22)),
                ('Expenses', models.IntegerField()),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Date_of_Visit', models.DateField()),
                ('Visit_Type', models.CharField(choices=[('Warrenty', 'Warrenty'), ('AMC', 'AMC'), ('Billable', 'Billable'), ('Installtion', 'Installtion')], max_length=15)),
                ('FCR_IR_SCR_Report_Number', models.IntegerField()),
                ('Call_Recived', models.DateField(blank=True)),
                ('Call_Attended', models.DateField(blank=True)),
                ('Call_Completed', models.DateField(blank=True)),
                ('Call_Status', models.CharField(choices=[('Completed', 'Completed'), ('Under Observation', 'Under Observation'), ('Pending', 'Pending')], max_length=17)),
                ('Voltage_earthing', models.CharField(blank=True, max_length=10)),
                ('Machine_type', models.CharField(max_length=30)),
                ('Machine_model', models.CharField(max_length=30)),
                ('Machine_serial_number', models.CharField(max_length=30)),
                ('Problem_Encountered', models.CharField(max_length=300)),
                ('Room_temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('Dust_free', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], max_length=5)),
                ('Solution_provided', models.CharField(max_length=300)),
                ('List_of_Spares_Used', models.CharField(blank=True, max_length=30)),
                ('List_of_Parts_Replaced', models.CharField(blank=True, max_length=30)),
                ('Customer_Comments', models.CharField(blank=True, max_length=30)),
                ('Customer_Feedback', models.CharField(blank=True, max_length=30)),
                ('Remark', models.CharField(blank=True, max_length=300, null=True)),
                ('Company_Name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='expense.customer_data')),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='expense_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
