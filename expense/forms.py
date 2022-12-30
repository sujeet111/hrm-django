from django import forms
from .models import Expense_data,Customer_data
from django.utils import timezone
from datetime import datetime

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expense_data
        widgets = {
		    'Date_of_Visit' : forms.DateInput(attrs={'class ': 'form-control','type':'date'}),
		    'Customer_City':forms.TextInput( attrs={'required': True}),
		    'Call_Recived':forms.DateInput(attrs={'class ': 'form-control datetimepicker-input','type':'date'}),
		    'Call_Attended':forms.DateInput(attrs={'class ': 'form-control datetimepicker-input','type':'date'}),
		    'Call_Completed':forms.DateInput(attrs={'class ': 'form-control datetimepicker-input','type':'date'}),
            'Remark': forms.Textarea(attrs={'rows': 3}),

        }
        fields = [ 
            'Expense_category',
            'Company_Name', 
            'Date_of_Visit', 
            'Visit_purpose',
            'Visit_Type',
            'Expenses',
            'FCR_IR_SCR_Report_Number',
            # -------------------------
            'Call_Recived',
            'Call_Attended',
            'Call_Completed',
            'Call_Status',
            'Voltage_earthing',
            # -------------------------
            'Machine_type',
            'Machine_model',
            'Machine_serial_number',
            # -------------------------
            'Problem_Encountered',
            'Solution_provided',
            # -------------------------
            'Room_temperature',
            'Dust_free',
            # -------------------------
            'List_of_Spares_Used',
            'List_of_Parts_Replaced',
            # -------------------------
            'Customer_Comments',
            'Remark']
    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class Customer_form(forms.ModelForm):
    class Meta:
        model = Customer_data
        fields = ['name', 'address', 'city', 'ph_number', 'email', 'Contact_person']
    def __init__(self, *args, **kwargs):
        super(Customer_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'