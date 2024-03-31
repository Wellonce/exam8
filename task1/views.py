from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from task1.models import CustomUser

from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect(request, 'login')  # Redirect to login page after registration
        else:
            messages.error(request, 'Registration form is invalid. Please correct the errors.')
            return render(request, 'registration_form.html', {'form': form})
    else:
        unique_field = request.GET.get('unique_field')
        user = CustomUser.objects.filter(unique_field=unique_field, is_deleted=True).first()
        if user:
            user.is_deleted = False
            user.save()
            authenticated_user = authenticate(username=user.username, password=user.password)
            if authenticated_user is not None:
                request.user = authenticated_user  # Set user in request object
                return redirect(request, 'home')
            else:
                messages.error(request, 'Authentication failed.')
        else:
            form = UserCreationForm()
            return render(request, 'registration_form.html', {'form': form})
        

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_deleted:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login or user is deleted.'})
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')


# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and not user.is_deleted:
#                 login(request, user)
#                 return redirect(request, 'home')  # Redirect to the home page after successful login
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})



