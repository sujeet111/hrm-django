from django.db import models
from django.contrib.auth.models import User



class customers(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    ph_number = models.IntegerField()
    email = models.EmailField(max_length = 254)#
    date_added = models.DateTimeField()

class expense_data(models.Model):
	visit_type = [('WR','WARRENTY'), 
				  ('AM','AMC'),
				  ('BI','BILLABLE'),
				  ('IN','INSTALLTION')]
	call_status = [("CO","COMPLETED"),
				   ("UO","UNDER OBSERVATION"),
				   ("PE","PENDING")]
	# machine_type = []
	visit_purpose = [('SA','Sales'),
					 ('IN','Installtion'),
					 ('CS',"Customer Support"),
					 ("SV","Site Visit"),
					 ("PM","Preventive Maintenance"),]
	dust_free_choice = [('y','Yes'),
					   ("n",'No'),
					   ("m",'Maybe')]
	
	Timestamp = models.DateTimeField(auto_now_add=True)
	Customer_Name = models.CharField(max_length=30)
	DATE_OF_VISIT =  models.DateField()
	Visit_Type = models.CharField(max_length=2,choices=visit_type)
	Customer_City = models.CharField(max_length=30)
	Contact_person = models.CharField(max_length=30)
	FCR_IR_SCR_REPORT_NUMBER = models.IntegerField()
	
	CALL_RECEIVED_D_T = models.DateField()
	CALL_ATTEND_D_T = models.DateField()
	CALL_COMPLETED_D_T = models.DateField()
	CALL_STATUS = models.CharField(max_length=2,choices=call_status)
	MACHINE_TYPE = models.CharField(max_length=30)
	MACHINE_MODEL = models.CharField(max_length=30)
	MACHINE_SERIAL_NUMBER = models.CharField(max_length=30)
	SOLUTION_PROVIDED_TO_CUSTOMER = models.CharField(max_length=30)
	ROOM_TEMPERATURE = models.IntegerField()
	DUST_FREE = models.CharField(max_length=2,choices=dust_free_choice)
	VOLTAGE_EARTHING = models.CharField(max_length=10)
	LIST_OF_SPARES_USED = models.CharField(max_length=30)
	CUSTOMER_FEEDBACK = models.CharField(max_length=30)
	CUSTOMER_COMMENTS = models.CharField(max_length=30)
	ENGINEER_SIGN_NAME_ON_REPORT = models.BooleanField()#bool
	MACHINE_OPERATOR_NAME_ON_REPORT = models.BooleanField()#bool
	CUSTOMER_SIGN_STAMP_NAME_ON_REPORT = models.BooleanField()#bool
	NAME_OF_THE_ENGINEER_CALL_ATTENDED = models.ForeignKey(User, on_delete=models.CASCADE)#user
	VISIT_PURPOSE = models.CharField(max_length=2,choices=visit_purpose)
	LIST_OF_PARTS_REPLACED = models.CharField(max_length=30)
	
	EXPENSES = models.IntegerField()
	REMARK = models.CharField(max_length=30)
	COMPANY_NAME = models.CharField(max_length=30)
	ADDRESS = models.CharField(max_length=30)
	MOBILE_NUMBER = models.IntegerField()
	REQUIREMENTS = models.CharField(max_length=30)
	EMAIL_ID = models.EmailField(max_length = 254)#email
	
	SCREEN_SIZESREQUITMEMT_DETAILS = models.CharField(max_length=30)#blank
	MEETING_DETAILS = models.CharField(max_length=30)#blank
	NEXT_FOLLOW_UP_DATE = models.CharField(max_length=30)#blank
	ORDER_STATUS = models.CharField(max_length=30)#blank
