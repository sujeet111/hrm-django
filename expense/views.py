from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Expense_data,Customer_data
from .forms import ExpensesForm, Customer_form
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime




# Create your views here.


@login_required(login_url= '/')
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_active:
            sum_amount=0
            if request.user.is_superuser:
                field = Expense_data.objects.all()
            else:
                field = Expense_data.objects.filter(created_by_id=request.user.id)
            for i in field:
                if i.Approved_status==True:
                    sum_amount = sum_amount + i.Expenses
            return render(request,'dashboard.html', {'field':field,'sum_amount':sum_amount})
        messages.warning(request,'Account No Longer Valid.')
        return redirect()
    
    return redirect()

#Expanse Detail view-----------------------------------------------------------------
@login_required(login_url= '/')
def detailexpense_view(request,id):
    if request.user.is_active:
        field = Expense_data.objects.get(id=id)
        print(field.Company_Name_id)
        companyname = Customer_data.objects.get(id=field.Company_Name_id)
        return render(request,'detailview.html', {'field':field,'companyname':companyname})
    messages.warning(request,'Account No Longer Valid.')
    return redirect()
    
@login_required(login_url= '/')
def add_expense(request):
    data={}
    if request.user.is_authenticated:
        if request.user.is_active:
            form = ExpensesForm(request.POST)
            if request.method == 'POST':
                if form.is_valid():
                    form.instance.created_by = request.user
                    form.save()
                    messages.success(request,'Expense Created')
                    return redirect('dashboard')
                else:
                    messages.error(request,'Expense Created')
                    data['error'] = 'Error'
            else:
                data = {'form':form}
                return render(request,'addexpense.html',data)
        else:
            return redirect('dashboard')
    else:
        return redirect('dashboard')

@login_required(login_url= '/')
def update_expense(request,id):
    if request.user.is_authenticated:
        if request.user.is_active:
            if request.user.is_superuser:
                data = Expense_data.objects.get(id=id)
            else:
                data = Expense_data.objects.get(id=id,created_by_id=request.user)
            if request.method=='POST':
                form = ExpensesForm(request.POST,instance=data)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Expense data updated.')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'form Error.')
            else:
                form = ExpensesForm(instance=data)
                return render(request,'addexpense.html',{'form':form})

@login_required(login_url= '/')
def delete_expense(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=='POST':
                messages.error(request,'Invalid Request')
                return redirect('dashboard')
            else:
                customer = Expense_data.objects.get(id=id).delete()
                messages.success(request,'Expense deleted successfuly')
                return redirect('dashboard')

@login_required(login_url= '/')
def reject_expese(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=='POST':
                return redirect('dashboard')
            else:
                Expense_data.objects.filter(id=id).update(Approved_status=False,Approved_by=request.user,Approved_Timestamp=datetime.now())
                return redirect('dashboard')

@login_required(login_url= '/')
def approve_expese(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=='POST':
                return redirect('dashboard')
            else:
                Expense_data.objects.filter(id=id).update(Approved_status=True,Approved_by=request.user,Approved_Timestamp=datetime.now())
                return redirect('dashboard')





# -----------------------------------------------------------------
@login_required(login_url= '/')
def customer_view(request):
    data={}
    form = Customer_form(request.POST)
    data = {'form':form}
    if request.user.is_authenticated:
        if request.user.is_active:
            if request.method == 'POST':
                if form.is_valid():
                    form.instance.created_by=request.user
                    form.save()
                    messages.success(request,'Customer Profile Created')
                    return redirect('Manage Customer')
                else:
                    print(form.errors)
            else:
                data['field'] = Customer_data.objects.all()
                return render(request,'customer.html',data)
            
        else:
            return redirect('dashboard')

@login_required(login_url= '/')
def customer_del(request,id):
    if request.user.is_authenticated:
        if request.user.is_active:
            if request.method=='POST':
                return redirect('dashboard')
            else:
                customer = Customer_data.objects.get(id=id).delete()
                return redirect('Manage Customer')
                    
@login_required(login_url= '/')
def customer_disable(request,id):
    if request.user.is_authenticated:
        if request.user.is_active:
            if request.method=='POST':
                return redirect('dashboard')
            else:
                Customer_data.objects.get(id=id).update(status=False)
                return redirect('Manage Customer')

@login_required(login_url= '/')
def customer_enable(request,id):
    if request.user.is_authenticated:
        if request.user.is_active:
            if request.method=='POST':
                return redirect('dashboard')
            else:
                Customer_data.objects.get(id=id).update(status=True)
                return redirect('Manage Customer')

@login_required(login_url= '/')
def customer_update(request,id):
    if request.user.is_authenticated:
        if request.user.is_active:
            data=Customer_data.objects.get(id=id)
            if request.method=='POST':
                form = Customer_form(request.POST,instance=data)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Customer profile updated.')
                    return redirect('Manage Customer')
                else:
                    messages.error(request, 'form Error.')
            else:
                form = Customer_form(instance=data)
                return render(request,'updatecustomer.html',{'form':form})


@login_required(login_url= '/')
def analytics(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=='GET':
                customers=Customer_data.objects.all()
                data={}
                for i in customers:                    
                    data[i.id]=Expense_data.objects.filter(Company_Name_id=i.id)
                return render(request,'analytics.html',data)