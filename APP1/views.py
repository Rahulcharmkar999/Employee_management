from django.shortcuts import render
from Employee_management.APP2.models import Employee, Company, Department

# Create your views here.
def base(request):
    return render( request, 'base.html')
def home(request):
    return render(request, 'home.html', {
        'total_employees': Employee.objects.count(),
        'total_companies': Company.objects.count(),
        'total_departments': Department.objects.count(),
        'recent_employees': Employee.objects.select_related('company', 'department').order_by('-id')[:5],
    })

def about(request):
    return render( request, 'about.html')

def contact(request):
    return render( request, 'contact.html')
