from django.shortcuts import render,redirect
from employeeapp.models import Employee
from django.core.paginator import Paginator



def home(request):
    return render(request, 'employeeapp/home.html')


def add_emp(request):
    gender_choices = Employee.Gender_Choices
    print(request.POST)

    if request.method == 'POST':
        name = request.POST.get('ename')
        gender = request.POST.get('egender')
        mob_num = request.POST.get('emobnum')
        email = request.POST.get('email')
        address = request.POST.get('eaddress')
        salary = request.POST.get('esalary')
        designation = request.POST.get('edesign')
        photo = request.FILES.get('photo')


        # if name and emp_id and gender and mob_num and email and address and salary and designation:
        obj = Employee(name = name, gender = gender, mob_num = mob_num, email = email, address = address,
                        salary = salary, designation = designation, photo = photo)

        obj.save()

        return redirect('/forms/list')
        
    return render(request, 'employeeapp/add.html', {'gender_choices' : gender_choices})
        
# def list_of_emp(request):
#     context = {
#         'data' : Employee.objects.all()
#     }

#     return render(request, 'employeeapp/list.html', context)

# from django.core.paginator import Paginator
# from .models import Employee

def list_of_emp(request):
    query = request.GET.get('q', '')
    employees = Employee.objects.filter(name__icontains=query) if query else Employee.objects.all()

    paginator = Paginator(employees, 5)  # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employeeapp/list.html', {'data': page_obj})


def details_of_emp(request,id):
    context = {
        'obj' : Employee.objects.get(pk = id)
    }
    return render(request, 'employeeapp/details.html',context)

def delete_emp(request,id): 
    obj = Employee.objects.get(pk=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('/forms/list/')
    
    context = {
        'obj' : Employee.objects.get(pk = id)
    }
    return render(request, 'employeeapp/delete.html',context)

def update_emp(request,id):

    obj = Employee.objects.get(pk=id)

    if request.method == 'POST':

        updated_name = request.POST.get('ename')
        updated_gender = request.POST.get('egender')
        updated_mob_num = request.POST.get('emobnum')
        updated_email = request.POST.get('email')
        updated_address = request.POST.get('eaddress')
        updated_salary = request.POST.get('esalary')
        updated_designation = request.POST.get('edesign')

        if 'photo' in request.FILES:
            obj.photo = request.FILES['photo']


        obj.name = updated_name
        obj.gender = updated_gender
        obj.mob_num = updated_mob_num
        obj.email = updated_email
        obj.address = updated_address
        obj.salary = updated_salary
        obj.designation = updated_designation

        obj.save()

        return redirect(f'/forms/details/{obj.id}/')

    context = {
        'obj' : Employee.objects.get(pk=id)
    }

    return render(request, 'employeeapp/update.html', context)

