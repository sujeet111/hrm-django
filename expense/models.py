from django.db import models
from django.contrib.auth.models import User
from django.conf import settings





class Customer_data(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    ph_number = models.IntegerField()
    email = models.EmailField(max_length = 254)#
    date_added = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_by',default=None,null=True,blank=True)
    Contact_person = models.ForeignKey(User, on_delete=models.CASCADE)#user
    def __str__(self):
        return self.name


class Expense_data(models.Model):
	visit_type = [('WARRENTY','WARRENTY'), 
				  ('AMC','AMC'),
				  ('BILLABLE','BILLABLE'),
				  ('INSTALLTION','INSTALLTION')]
	Call_status = [("COMPLETED","COMPLETED"),
				   ("UNDER OBSERVATION","UNDER OBSERVATION"),
				   ("PENDING","PENDING")]
	# Machine_type = []
	visit_purpose = [('Sales','Sales'),
					 ('Installtion','Installtion'),
					 ('Customer Support',"Customer Support"),
					 ("Site Visit","Site Visit"),
					 ("Preventive Maintenance","Preventive Maintenance"),]
	dust_free_choice = [('Yes','Yes'),
					   ("No",'No'),
					   ("Maybe",'Maybe')]
	expense_choice =[
        ('Travel and Accommodation','Travel and Accommodation'),
        ('Parts Replaced','Parts Replaced')]
	
	Timestamp = models.DateTimeField(auto_now_add=True)
	Date_of_visit =  models.DateField()
	Visit_type = models.CharField(max_length=15,choices=visit_type)
	FCR_IR_SCR_Report_Number = models.IntegerField()
	Call_recived_date_and_time = models.DateField()
	Call_attended_date_and_time= models.DateField()
	Call_completed_date_and_time= models.DateField()
    
	Machine_type = models.CharField(max_length=30)
	Machine_model = models.CharField(max_length=30)
	Machine_serial_number = models.CharField(max_length=30)
	Solution_provided= models.CharField(max_length=30)
	Room_temperature = models.CharField(max_length=10,blank=True,null=True)
	Dust_free = models.CharField(max_length=5,choices=dust_free_choice)
	Voltage_earthing = models.CharField(max_length=10,blank=True)
	List_of_spares_used = models.CharField(max_length=30,blank=True)
	Customer_feedback = models.CharField(max_length=30,blank=True)
	Customer_comments = models.CharField(max_length=30,blank=True)
	Engineer_sign_name_on_report = models.BooleanField()#Bool
	Machine_operator_name_on_report = models.BooleanField()#Bool
	Customer_sign_and_stamp_on_report = models.BooleanField()#Bool
	Name_of_the_engineer_call_attended = models.CharField(max_length=30)
	Visit_purpose = models.CharField(max_length=22,choices=visit_purpose)
	List_of_parts_replaced = models.CharField(max_length=30,blank=True)
	
	Expenses = models.IntegerField()
	Remark = models.CharField(max_length=30)
	Company_Name = models.ForeignKey(Customer_data, on_delete=models.CASCADE,default=None)
	Requirements = models.CharField(max_length=30)
	
	# Screen_sizes_requitmemt_details = models.CharField(max_length=30)#Blank
	# Meeting_details = models.CharField(max_length=30)#Blank
	# Next_follow_up_date = models.CharField(max_length=30)#Blank
	# Order_status = models.CharField(max_length=30)#Blank
	Approved_status = models.BooleanField(null=True)
	Expense_category=models.CharField(max_length=30,choices=expense_choice)
    
# blank=True, null=True