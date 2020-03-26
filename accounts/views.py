from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def login(request):
    '''
    Function used for Login
    '''
    if request.method == "POST":
        #    Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def register(request):
    '''
    Function used for registration
    '''

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check for validation
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, 'you are loggedin')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'you are registered and now login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        # messages.error(request, 'Testing error messages')

    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    '''
    Function used for Dashboard
    '''
    user_contacts = Contact.objects.all().filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    '''
    Function used for logout
    '''
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'you have been logged out')
        return redirect('index')
