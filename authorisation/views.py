from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
#python manage.py runserver

def login(request):
	if request.method == 'POST':
		email = request.POST['email'].replace(' ','').lower()
		password = request.POST['password1']

		user = auth.authenticate(username=email, password=password)

		if user:
			auth.login(request,newUser)
			return redirect('dashboard')

		else:
			messages.error(request, "Invalid Credentials or User does not Exist")
			return redirect('register')
	return render(request, 'authorisation/login.html', {})

def register(request):
	if request.method == 'POST':
		email = request.POST['email'].replace(' ','').lower()
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if not password1 == password2:
			messages.error(request, "Passwords do not match")
			return redirect('register')


		if User.objects.filter(email=email).exists():
			messages.error(request, "A user with the email address: {} already exists, Please try a different email".format(email))
			return redirect('register')


		newUser = User.objects.create_user(email=email, username=email, password=password1)
		newUser.save()


		auth.login(request,newUser)
		return redirect('dashboard')
	return render(request, 'authorisation/register.html', {})


def dashboard(request):
    return render(request, 'authorisation/dashboard.html', {})
