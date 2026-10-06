from django.contrib import admin

# Register your models here.
from .models import Employee, Company,Department
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','name','emails','age','salary','department','address','company')
    search_fields=('name','emails')
    ordering=('id',)
    list_filter=('company',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','name','emails','location','branch_number')
    search_fields=('name','emails')
    ordering=('id',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    ordering = ('id',)
 