import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ggiproject.wsgi import *
from ggiproject import settings
from django.template.loader import get_template
from customers.models import Customer
from products.models import Product
# from weasyprint import HTML, CSS
from .models import Expenses
import json


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required(login_url="/accounts/login/")
def expenses_list_view(request):
    context = {
        "active_icon": "expenses",
        "expenses": Expenses.objects.all()
    }
    return render(request, "expenses/expenses.html", context=context)


@login_required(login_url="/accounts/login/")
def expenses_add_view(request):
    context = {
        "active_icon": "expenses",
    }

    if request.method == 'POST':
        category = request.POST.get('category'),
        total = request.POST["grand_total"],
        description = request.POST['description']
        print(total)
        print(category[0])
        
        # expenses_attributes = {
        #     "Category": request.POST.get('category'),
        #     "grand_total": request.POST["grand_total"],
        # }
        
       
       
        
        try:
             
            expense = Expenses(
                Category = category[0],
                grand_total = int(total[0]),
                description = description
            )
            expense.save()
            
            print("Expenses saved")

            messages.success(
                request, 'Expenses created successfully!', extra_tags="success")

        except Exception as e:
            messages.success(
                request, 'There was an error during the creation!', extra_tags="danger")

        return redirect('expenses:expenses_list')

    return render(request, "expenses/expenses_add.html", context=context)


