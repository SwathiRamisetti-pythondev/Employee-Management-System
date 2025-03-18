from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, LatestNews, Calendar
from .forms import EmployeeForm, LatestNewsForm, CalendarForm
# Create your views here.
def homeview(request):
    return HttpResponse('<h1>Welcome to Employee Management System</h1>'
                        '<p>This is the home page.</p>'
                        '<a href="/hr/">Go to HR Manager</a>')

def hrview(request):
    return HttpResponse('<h1>HR Manager Portal</h1>'
                        '<button>Add Employee</button>'
                        '<button>View Employee Data</button>'
                        '<button>Add Latest News</button>'
                        '<button>Add Calendar</button>')
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_employees/')  # Redirect to employee list
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

# View for Displaying Employee Data
def view_employees(request):
    employees = Employee.objects.all()  # Fetch all employee records
    return render(request, 'view_employees.html', {'employees': employees})

# View for Adding Latest News
def add_news(request):
    if request.method == "POST":
        form = LatestNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_news/')
    else:
        form = LatestNewsForm()
    return render(request, 'add_news.html', {'form': form})

# View for Displaying Latest News
def view_news(request):
    news_list = LatestNews.objects.all()
    return render(request, 'view_news.html', {'news_list': news_list})

# View for Adding Calendar Event
def add_calendar(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_calendar/')
    else:
        form = CalendarForm()
    return render(request, 'add_calendar.html', {'form': form})

# View for Displaying Calendar Data
def view_calendar(request):
    calendar_list = Calendar.objects.all()
    return render(request, 'view_calendar.html', {'calendar_list': calendar_list})