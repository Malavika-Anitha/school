from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from capp.models import Student, Department, Course, Material


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('credentials:register')

            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                return redirect('credentials:login')
            print('user created')

        else:
            messages.info(request,'password not matched')
            return redirect('credentials:register')
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        passw=request.POST['pass']
        user=auth.authenticate(username=username,password=passw)

        if user is not None:
            auth.login(request,user)
            return redirect('credentials:dashboard')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('credentials:login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def dashboard(request):
    return render(request,'dashboard.html')


def order(request):
    if request.method == 'POST':
        # Get data from the POST request
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        department_id = request.POST.get('department')
        course_id = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials_provide = request.POST.getlist('materials_provide')

        # Create a new Student instance and save it to the database
        student = Student.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            department_id=department_id,
            course_id=course_id,
            purpose=purpose,


        )

        # Add materials provided by the student
        student.materials_provide.set(materials_provide)

        messages.success(request, 'Form submitted successfully!')
        return redirect('credentials:success')

    # Get the list of departments, courses, and materials to pass to the template
    departments = Department.objects.all()
    courses = Course.objects.all()
    materials = Material.objects.all()

    return render(request, 'order.html', {'departments': departments, 'courses': courses, 'materials': materials})

def success(request):
    return render(request,'orderconfirm.html')