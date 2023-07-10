from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name='default'),
    path('search', views.search, name='search'),
    path('date_search', views.date_search, name='date_search'),
    path('treeview',views.tree_view, name='treeview'),
    path('sort_name', views.sort_by_name, name='sort_name'),
    path('sort_by_surname', views.sort_by_surname, name='sort_by_surname'),
    path('sort_by_birthday', views.sort_by_birthday, name='sort_by_birthday'),
    path('sort_by_employeenum', views.sort_by_employeenum, name='sort_by_employeenum'),
    path('sort_by_salary', views.sort_by_salary, name='sort_by_salary'),
    path('sort_by_role', views.sort_by_role, name='sort_by_role'),
    path('sort_by_reporting', views.sort_by_reporting, name='sort_by_reporting'),
]
