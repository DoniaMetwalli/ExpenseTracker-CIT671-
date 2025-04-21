from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Expense
# from .forms import ExpenseForm

# Create your views here.

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses' : expenses})

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'expense_detail.html', {'expense': expense})