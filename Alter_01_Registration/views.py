# from django.shortcuts import  render, redirect
# from .forms import NewUserForm()
# from django.contrib.auth import login
# from django.contrib import messages

# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("Alter_01_Registration:index")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="Alter_01_Registration/register.html", context={"register_form":form})


# def Insertrecord(request):
#     if request.method=='POST':
#         if request.POST.get('UserName') and request.POST.get('Password') and request.POST.get('Email'):
#             saverecord=UsrInsert()
#             saverecord.UserName=request.POST.get('UserName')
#             saverecord.Password=request.POST.get('Password')
#             saverecord.Email=request.POST.get('Email')
#             saverecord.save()
#             messages.success(request,'Log in Successful..!!!')
#             return render(request,'user-login.html')
#     else:
#             return render(request,'user-login.html')
#
# def Userregistration(request):
#     if request.method=='POST':
#         if request.POST.get('username') and request.POST.get('email') and request.POST.get('password'):
#             saverecords=UsrRegister()
#             saverecords.username=request.POST.get('username')
#             saverecords.email=request.POST.get('email')
#             saverecords.password=request.POST.get('password')
#             saverecords.save()
#             messages.success(request, 'Registration Successful..!!!')
#             return render(request,'user-login.html')
#     else:
#             return render(request,'user-login.html')