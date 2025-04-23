# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add/', views.add_expense, name='add_expense'),
# ]

from django.urls import path, include
from .views import ExpenseViewSet, expense_list_view, add_expense_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', expense_list_view, name='home'),
    path('add/', add_expense_view, name='add_expense'),
    path('api/', include(router.urls)),
]

