import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee

def index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})

@csrf_exempt
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emp  = Employee.objects.create(
            name=data['name'], email=data['email'],
            department=data['department'], salary=data['salary']
        )
        return JsonResponse({'id': emp.id, 'name': emp.name, 'email': emp.email,
                             'department': emp.department, 'salary': str(emp.salary)})

@csrf_exempt
def update(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        emp  = Employee.objects.get(id=id)
        emp.name = data['name']; emp.email = data['email']
        emp.department = data['department']; emp.salary = data['salary']
        emp.save()
        return JsonResponse({'message': 'Updated successfully'})

@csrf_exempt
def delete(request, id):
    if request.method == 'DELETE':
        Employee.objects.get(id=id).delete()
        return JsonResponse({'message': 'Deleted successfully'})
