# from django.shortcuts import render, redirect
# from .models import Expense
# from .forms import ExpenseForm

# def home(request):
#     expenses = Expense.objects.all()
#     return render(request, 'expenses/home.html', {'expenses': expenses})

# def add_expense(request):
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ExpenseForm()
#     return render(request, 'expenses/add_expense.html', {'form': form})
from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer