from django.urls import path
from employeeapp.views import *


urlpatterns = [
    path('home/',home),
    path('add/',add_emp),
    path('list/',list_of_emp),
    path('details/<int:id>/',details_of_emp),
    path('delete/<int:id>/',delete_emp),
    path('update/<int:id>/',update_emp),
]
