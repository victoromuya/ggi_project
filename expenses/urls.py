from django.urls import path

from . import views

app_name = "expenses"
urlpatterns = [
    # List expenses
    path('', views.expenses_list_view, name='expenses_list'),
    # Add expenses
    path('add', views.expenses_add_view, name='expenses_add'),
]