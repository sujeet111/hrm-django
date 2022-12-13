from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import expense_data
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = expense_data
        widgets = {
            'Visit_Type': forms.TextInput(attrs={'class': 'form-control'}),
            'Timestamp': forms.DateTimeField(),
		    'Customer_Name': forms.TextInput(),
		    'DATE_OF_VISIT' : forms.DateInput(),
		    'Visit_Type': forms.Select(),
		    'Customer_City':forms.TextInput(),
		    'Contact_person':forms.Select(),
		    'FCR_IR_SCR_REPORT_NUMBER':forms.NumberInput(),
		    'CALL_RECEIVED_D_T':forms.DateInput(),
		    'CALL_ATTEND_D_T':forms.DateInput(),
		    'CALL_COMPLETED_D_T':forms.DateInput(),
		    'CALL_STATUS':forms.Select(),
		    'MACHINE_TYPE':forms.TextInput(),
		    'MACHINE_MODEL':forms.TextInput(),
		    'MACHINE_SERIAL_NUMBER':forms.NumberInput(),
		    'SOLUTION_PROVIDED_TO_CUSTOMER':forms.TextInput(),
		    'ROOM_TEMPERATURE':forms.TextInput(),
		    'DUST_FREE':forms.TextInput(),
		    'VOLTAGE_EARTHING': forms.TextInput(),
		    'LIST_OF_SPARES_USED': forms.TextInput(),
		    'CUSTOMER_FEEDBACK':forms.TextInput(),
		    'CUSTOMER_COMMENTS':forms.TextInput(),
		    'ENGINEER_SIGN_NAME_ON_REPORT':forms.TextInput(),
		    'MACHINE_OPERATOR_NAME_ON_REPORT':forms.TextInput(),
		    'CUSTOMER_SIGN_STAMP_NAME_ON_REPORT':forms.TextInput(),
		    'NAME_OF_THE_ENGINEER_CALL_ATTENDED':forms.TextInput(),
		    'VISIT_PURPOSE': forms.Select(),
		    'LIST_OF_PARTS_REPLACED':forms.TextInput(),
		    'EXPENSES': forms.NumberInput(),
		    'REMARK':forms.TextInput(),
		    'COMPANY_NAME':forms.TextInput(),
		    'ADDRESS':forms.TextInput(),
		    'CONTACT_PERSON':forms.TextInput(),
		    'MOBILE_NUMBER':forms.TextInput(),
		    'REQUIREMENTS':forms.TextInput(),
		    'EMAIL_ID':forms.EmailInput(),
		    'SCREEN_SIZES':forms.TextInput(),
		    'REQUITMEMT_DETAILS':forms.TextInput(),
		    'MEETING_DETAILS':forms.TextInput(),
		    'NEXT_FOLLOW_UP_DATE':forms.DateInput(),
		    'ORDER_STATUS':forms.TextInput(),

        }
        fields = ['title' , 'date', 'amount','invoice']