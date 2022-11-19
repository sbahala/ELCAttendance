from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request, "attendanceApp/index.html")

def signup(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST.get('fname')
        #fname = request.POST['fname']
        lname = request.POST.get('lname')
        #lname = request.POST['lname']
        email = request.POST.get('email')
        #email = request.POST['email']
        #pass1 = request.POST['pass1']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        #pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your acount has been successfully created.")
        return redirect ('login')

    return render(request, "attendanceApp/signup.html")

def signin(request):

    if request.method =='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"attendanceApp/index.html",{'fname':fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "attendanceApp/signin.html")

def logout(request):
    #logout(request)
    #messages.success(request,"Logged Out Successfully")
    return redirect(request, "attendanceApp/index.html")
    #pass

# def student_view_attendance(request):
#     return render(request, "attendanceApp/student_view_attendance.html")
   