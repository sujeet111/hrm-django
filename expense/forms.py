from django import forms
from .models import Expense_data,Customer_data
from django.utils import timezone
from datetime import datetime

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expense_data
        widgets = {
      #       'Timestamp': forms.DateTimeField(),
		    # 'Company_Name': forms.Select(attrs={'class ': 'form-control'}),
      #       'Expense_category':forms.Select(attrs={'class ': 'form-control'}),
		    'Date_of_visit' : forms.DateInput(attrs={'class ': 'form-control','type':'date'}),
		    # 'Visit_type': forms.Select(attrs={'class ': 'form-control'}),
		    'Customer_City':forms.TextInput( attrs={'required': True}),
		    # # 'FCR_IR_SCR_REPORT_NUMBER':forms.NumberInput( attrs={'required': True}),
		    'Call_recived_date_and_time':forms.DateInput(attrs={'class ': 'form-control datetimepicker-input','type':'date'}),
		    'Call_attended_date_and_time':forms.DateInput(attrs={'class ': 'form-control datetimepicker-input','type':'date'}),
		    'Call_completed_date_and_time':forms.DateInput(attrs={'class ': 'form-control datetimepicker-input','type':'date'}),
		    # 'CALL_STATUS':forms.Select( attrs={'required': True}),
		    # 'MACHINE_TYPE':forms.TextInput( attrs={'required': True}),
		    # 'MACHINE_MODEL':forms.TextInput( attrs={'required': True}),
		    # 'MACHINE_SERIAL_NUMBER':forms.NumberInput(),
		    # 'Solution_Provided':forms.TextInput( attrs={'required': True}),
		    # 'ROOM_TEMPERATURE':forms.NumberInput(),
		    # 'DUST_FREE':forms.Select(),
		    # 'VOLTAGE_EARTHING': forms.TextInput(),
		    # 'LIST_OF_SPARES_USED': forms.TextInput(),
		    # 'CUSTOMER_FEEDBACK':forms.TextInput(),
		    # 'CUSTOMER_COMMENTS':forms.TextInput(),
		    'Engineer_sign_name_on_report':forms.NullBooleanSelect(),
		    'Machine_operator_name_on_report':forms.NullBooleanSelect(),
		    'Customer_sign_and_stamp_on_report':forms.NullBooleanSelect(),
		    # 'VISIT_PURPOSE': forms.Select(),
		    # 'LIST_OF_PARTS_REPLACED':forms.TextInput(),
		    # 'EXPENSES': forms.NumberInput(),
		    # 'REMARK':forms.TextInput(),
		    # 'COMPANY_NAME':forms.TextInput(),
		    # 'ADDRESS':forms.TextInput(),
		    # 'MOBILE_NUMBER':forms.TextInput(),
		    # 'REQUIREMENTS':forms.TextInput(),
		    # 'EMAIL_ID':forms.EmailInput(),
		    # # 'SCREEN_SIZES':forms.TextInput(),
		    # # 'REQUITMEMT_DETAILS':forms.TextInput(),
		    # 'MEETING_DETAILS':forms.TextInput(),
		    # 'NEXT_FOLLOW_UP_DATE':forms.DateInput(attrs={'class ': 'form-control','type':'date'}),
		    # 'ORDER_STATUS':forms.TextInput(),

        }
        fields = [ 
            'Expense_category',
            'Company_Name', 
            'Date_of_visit', 
            'Visit_type',
            'FCR_IR_SCR_Report_Number',
            'Call_recived_date_and_time',
            'Call_attended_date_and_time',
            'Call_completed_date_and_time',
            'Machine_type',
            'Machine_model',
            'Machine_serial_number',
            'Solution_provided',
            'Room_temperature',
            'Dust_free',
            'Voltage_earthing',
            'List_of_spares_used',
            'Customer_feedback',
            'Customer_comments',
            
            'Visit_purpose',
            'List_of_parts_replaced',
            'Expenses',
            'Remark',
            'Requirements',

            'Engineer_sign_name_on_report',
            'Machine_operator_name_on_report',
            'Customer_sign_and_stamp_on_report',
            'Name_of_the_engineer_call_attended',
            # Screen_sizes_requitmemt_details,
            # Meeting_details,
            # Next_follow_up_date,
            # 'Order_status',
            
            ]
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