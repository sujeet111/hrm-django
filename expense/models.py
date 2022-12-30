from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Customer_data(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    ph_number = models.CharField(max_length=10)
    email = models.EmailField(max_length = 254)#
    date_added = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_by',default=None,null=True,blank=True)
    Contact_person = models.ForeignKey(User, on_delete=models.CASCADE)#user
    def __str__(self):
        return self.name


class Expense_data(models.Model):
    visit_type = [('Warrenty','Warrenty'), 
                  ('AMC','AMC'),
                  ('Billable','Billable'),
                  ('Installtion','Installtion')]
    Call_status = [("Completed","Completed"),
                   ("Under Observation","Under Observation"),
                   ("Pending","Pending")]
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
    
    
    Approved_status = models.BooleanField(null=True)
    Approved_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='expense_approved_by',null=True,default=None)
    Approved_Timestamp = models.DateTimeField(blank=True)
    # ----------------------------------------------------------------
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='expense_created_by',default=None)
    Expense_category=models.CharField(max_length=30,choices=expense_choice)
    Visit_purpose = models.CharField(max_length=22,choices=visit_purpose)
    Company_Name = models.ForeignKey(Customer_data, on_delete=models.CASCADE,default=None)
    Expenses = models.IntegerField()
    # ----------------------------------------------------------------
    Timestamp = models.DateTimeField(auto_now_add=True)
    Date_of_Visit =  models.DateField()
    Visit_Type = models.CharField(max_length=15,choices=visit_type)
    # ----------------------------------------------------------------
    FCR_IR_SCR_Report_Number = models.IntegerField()
    Call_Recived = models.DateField(blank=True)
    Call_Attended= models.DateField(blank=True)
    Call_Completed= models.DateField(blank=True)
    Call_Status = models.CharField(max_length=17,choices=Call_status)
    Voltage_earthing = models.CharField(max_length=10,blank=True)
    # ----------------------------------------------------------------
    Machine_type = models.CharField(max_length=30)
    Machine_model = models.CharField(max_length=30)
    Machine_serial_number = models.CharField(max_length=30)
    # ----------------------------------------------------------------
    Problem_Encountered = models.CharField(max_length=300)
    Room_temperature = models.CharField(max_length=10,blank=True,null=True)
    Dust_free = models.CharField(max_length=5,choices=dust_free_choice)
    Solution_provided= models.CharField(max_length=300)
    # ----------------------------------------------------------------
    List_of_Spares_Used = models.CharField(max_length=30,blank=True)
    List_of_Parts_Replaced = models.CharField(max_length=30,blank=True)
    # ----------------------------------------------------------------
    Customer_Comments = models.CharField(max_length=30,blank=True)
    Customer_Feedback = models.CharField(max_length=30,blank=True)
    # ----------------------------------------------------------------
    Remark = models.CharField(max_length=300,blank=True,null=True)

    
# blank=True, null=True