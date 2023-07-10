from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeeTable
from itertools import chain

# Create your views here.
def default_view(request):
    """
    This is the default landing page.

    It loads whatever is in the model into a queryset.
    The queryset is served as a dict context for the
    html template. 
    In summary, Get model objects. Send to front for display.

    Args:
        request:   Requires an httprequest object.

    Returns:
        HttpResponse.

    Raises:
        Unknown
    """
    # Get model objects. Send to front for display
    emp_table = EmployeeTable.objects.all()
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False})


def search(request):
    """
    Gets a search query from the request object parameter.

    Checks if the request is kosher and then builds a set
    containing entries which have at least one matching
    attribute. 
    In summary, fuzzy search.

    Args:
        request:   Requires an httprequest object.
        POST:      Will only work if a post request is made

    Returns:
        HttpResponse.
    """
    if request.method == "POST":
        query_name = request.POST.get('search',None)

        if query_name:

            # Search each field except date
            emp_table_name = EmployeeTable.objects.filter(Name__contains=query_name)
            emp_table_surname = EmployeeTable.objects.filter(Surname__contains=query_name)
            emp_table_emplnum = EmployeeTable.objects.filter(Employee_Number__contains=query_name)
            emp_table_salary = EmployeeTable.objects.filter(Salary__contains=query_name)
            emp_table_role = EmployeeTable.objects.filter(Role_Description__contains=query_name)
            emp_table_reporting = EmployeeTable.objects.filter(Reporting_Line__contains=query_name)

            # Combine Results
            emp_table_full = chain(emp_table_name,emp_table_surname,emp_table_emplnum,emp_table_role, emp_table_salary, emp_table_reporting)
            return render(request,'home.html',{'EmpTable':emp_table_full, 'filter_applied':True})
        
        else:
            return render(request,'home.html',{'EmpTable':None, 'filter_applied':False})

def date_search(request):
    """
    Gets a search query from the request object parameter.

    Checks if the request is kosher and then converts the 
    date values to string in order to compare, then builds 
    and returns a query set of objects matching the criteria

    Args:
        request:   Requires an httprequest object.
        POST:      Will only work if a post request is made

    Returns:
        HttpResponse.
    """
    if request.method == "POST":
        query_from = request.POST.get('date_from',None)
        query_to = request.POST.get('date_to',None)

        emp_table = EmployeeTable.objects.all()
        temp_table = []
        if query_from and query_to:
            for i in emp_table:
                if (str(i.Birth_Date) > query_from) and (str(i.Birth_Date) < query_to):
                    temp_table.append(i)
            return render(request,'home.html',{'EmpTable':temp_table, 'filter_applied':True})

    return render(request,'home.html',{'EmpTable':None, 'filter_applied':False})


def tree_view(request):
    """
    For separation of concerns.

    This loads the data from the model and
    splits it into roles. Individual role 
    querysets are then frontend processed
    to make the tree graph.

    Args:
        request:   Requires an httprequest object.

    Returns:
        HttpResponse.
    """
    emp_table_exec = EmployeeTable.objects.filter(Reporting_Line__contains="None")
    emp_table_man = EmployeeTable.objects.filter(Reporting_Line__contains="Executive")
    emp_table_emp = EmployeeTable.objects.filter(Reporting_Line__contains="Manager")
    emp_table_train = EmployeeTable.objects.filter(Reporting_Line__contains="Employee")
    return render(request,'treeview.html',{'executives':emp_table_exec,'managers':emp_table_man, 'employees':emp_table_emp,'trainees':emp_table_train})

def sort_by_name(request):
    """
    Serves the query set sorted by first names followed by surnames.
    """
    emp_table = EmployeeTable.objects.order_by('Name','Surname')
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False, 'sort':'name'})

def sort_by_surname(request):
    """
    Serves the query set sorted by surnames followed by first names.
    """
    emp_table = EmployeeTable.objects.order_by('Surname','Name')
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False, 'sort':'surname'})

def sort_by_birthday(request):
    """
    Serves the query set sorted by date descending (youngest first).
    """
    emp_table = EmployeeTable.objects.order_by('-Birth_Date','Name')
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False, 'sort':'birthday'})

def sort_by_employeenum(request):
    """
    Serves the query set sorted by employee number followed by first names.
    """
    emp_table = EmployeeTable.objects.order_by('Employee_Number','Name')
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False, 'sort':'employeenum'})

def sort_by_salary(request):
    """
    Serves the query set sorted by Salary (descending) followed by first names.
    """
    emp_table = EmployeeTable.objects.order_by('-Salary','Name')
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False, 'sort':'salary'})

def sort_by_role(request):
    """
    Serves the query set sorted by role followed by first names.
    """
    emp_table = EmployeeTable.objects.order_by('Role_Description','-Salary')
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False, 'sort':'role'})

def sort_by_reporting(request):
    """
    Serves the query set sorted by reporting line followed by first names.
    """
    emp_table = EmployeeTable.objects.order_by('Reporting_Line','-Salary')
    return render(request,'home.html',{'EmpTable':emp_table, 'filter_applied':False, 'sort':'reporting'})