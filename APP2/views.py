from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Company, Department


# READ
def display(request):
    data = Employee.objects.all()
    return render(request, 'empdata.html', {'employeedata': data})


# CREATE
def addEmpData(request):

    companies = Company.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        emails = request.POST.get('emails')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        address = request.POST.get('address')
        company_id = request.POST.get('company')
        department_id = request.POST.get('department')

        Employee.objects.create(
            name=name,
            emails=emails,
            age=age,
            salary=salary,
            address=address,
            company_id=company_id,
            department_id=department_id
        )

        return redirect('display')

    return render(request, 'add.html', {
        'companies': companies,
        'departments': departments
    })


# UPDATE
def updateEmpData(request, id):

    employee = get_object_or_404(Employee, id=id)

    companies = Company.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.emails = request.POST.get('emails')
        employee.age = request.POST.get('age')
        employee.salary = request.POST.get('salary')
        employee.address = request.POST.get('address')
        employee.company_id = request.POST.get('company')
        employee.department_id = request.POST.get('department')

        employee.save()

        return redirect('display')

    return render(request, 'update.html', {
        'employee': employee,
        'companies': companies,
        'departments': departments
    })


# DELETE
def deleteEmpData(request, id):

    employee = get_object_or_404(Employee, id=id)
    employee.delete()

    return redirect('display')