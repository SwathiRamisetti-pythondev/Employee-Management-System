from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Employee, LatestNews, Calendar
from .forms import EmployeeForm, LatestNewsForm, CalendarForm

# Function to check if user is an HR Manager
def is_hr_manager(user):
    return user.groups.filter(name='HR Manager').exists()

# Home Page

def homeview(request):
    return render(request, 'home.html')  # Properly render home.html

# HR Manager Portal (Restricted Access)
@login_required
@user_passes_test(is_hr_manager, login_url='/no-access/')
def hrview(request):
    return render(request, 'hr_manager.html')  # Now using a proper template


# Add Employee (Restricted Access + Validation)
@login_required
@user_passes_test(is_hr_manager, login_url='/no-access/')
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data.get('emp_id')
            if Employee.objects.filter(emp_id=emp_id).exists():
                form.add_error('emp_id', "An employee with this ID already exists!")
            else:
                form.save()
                return redirect('/view_employees/')  # Redirect to employee list
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

# View Employees (Accessible to all logged-in users)
@login_required
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'view_employees.html', {'employees': employees})


# Add Latest News (Restricted Access)
@login_required
@user_passes_test(is_hr_manager, login_url='/no-access/')
def add_news(request):
    if request.method == "POST":
        form = LatestNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_news/')
    else:
        form = LatestNewsForm()
    return render(request, 'add_news.html', {'form': form})

# View Latest News (Accessible to all logged-in users)
@login_required
def view_news(request):
    news_list = LatestNews.objects.all()
    return render(request, 'view_news.html', {'news_list': news_list})

# Add Calendar Event (Restricted Access)
@login_required
@user_passes_test(is_hr_manager, login_url='/no-access/')
def add_calendar(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_calendar/')
    else:
        form = CalendarForm()
    return render(request, 'add_calendar.html', {'form': form})

# View Calendar Data (Accessible to all logged-in users)
@login_required
def view_calendar(request):
    calendar_list = Calendar.objects.all()
    return render(request, 'view_calendar.html', {'calendar_list': calendar_list})

# No Access Page (For unauthorized users)
def no_access(request):
    return render(request, 'no_access.html')
def technical_issues(request):
    return render(request, 'technical_issues.html')
