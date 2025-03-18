from django import forms
from .models import Employee, LatestNews, Calendar

# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

# Latest News Form
class LatestNewsForm(forms.ModelForm):
    class Meta:
        model = LatestNews
        fields = '__all__'

# Calendar Form
class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'

