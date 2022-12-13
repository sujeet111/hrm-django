from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ExpensesForm

# Create your views here.


@login_required(login_url='/login/')
def dashboard(request):

    return render(request,'dashboard.html', {})
    
@login_required(login_url='/login/')
def add_expense(request):
        if request.user.is_authenticated:
            if request.user.is_active:
                form = ExpensesForm(request.POST or None, request.FILES or None)
                if request.method == 'POST':
                    if form.is_valid():
                        form.save()
                        alert = {'success':'success'}
                    return redirect('dashboard',alert)
                else:
                    data = {'form':form}
                    return render(request,'addexpense.html',data)
