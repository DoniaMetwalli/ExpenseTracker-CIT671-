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
from .serializers import ExpenseSerializer
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm 

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
def expense_list_view(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/home.html', {'expenses': expenses})

def add_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirects back to the home page after saving
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})