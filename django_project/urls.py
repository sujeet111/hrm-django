"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users.forms import UserLoginForm
from users import views as user_views
from expense import views as expense_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='users/login.html',authentication_form=UserLoginForm), name='login'),
    path('register/', user_views.register, name='register'),
# -----------------------------------------------------------------------------------------------------
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# -----------------------------------------------------------------------------------------------------
	path('dashboard/',expense_views.dashboard, name='dashboard'),
    path('detail_expense/<int:id>',expense_views.detailexpense_view, name='Detail Expense'),
    path('add_expense/',expense_views.add_expense,name='New Expense'),
    path("update_expense/<int:id>",expense_views.update_expense,name='Update Expense'),
    path("delete_expense/<int:id>",expense_views.delete_expense,name='Delete Expense'),
    path("approve_expense/<int:id>",expense_views.approve_expese,name='Approve Expense'),
    path("reject_expense/<int:id>",expense_views.reject_expese,name='Reject Expense'),

# -----------------------------------------------------------------------------------------------------
    path('managecustomer/',expense_views.customer_view,name='Manage Customer'),
    path('deletecustomer/<int:id>',expense_views.customer_del,name='Delete Customer'),
    path('disablecustomer/<int:id>',expense_views.customer_disable,name='Disable Customer'),
    path('enablecustomer/<int:id>',expense_views.customer_enable,name='Enable Customer'),
    path("updatecustomer/<int:id>",expense_views.customer_update,name='Update Customer'),
    path("analytics/",expense_views.analytics,name='Analytics'),
    
    
]



