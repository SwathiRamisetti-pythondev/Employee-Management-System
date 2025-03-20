from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    department = models.CharField(max_length=100)
    salary_package = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.IntegerField()

    def __str__(self):
        return self.emp_name

# Latest News Model
class LatestNews(models.Model):
    occasion = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.occasion[:50]

# Calendar Model (For Holidays)
class Calendar(models.Model):
    date = models.DateField()
    occasion = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.occasion}"

