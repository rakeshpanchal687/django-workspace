from django.http import HttpResponse
from django.shortcuts import render

from .utility.data_validator import DataValidator


def test_ors(request):
    return HttpResponse('<h1>ORS APP</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    form = {}
    form['message'] = ''
    form['input_error'] = {}
    form['input_error']['error'] = False

    if request.method == "POST":
        form['first_name'] = request.POST.get('firstName', '')
        form['last_name'] = request.POST.get('lastName', '')
        form['login_id'] = request.POST.get('loginId', '')
        form['password'] = request.POST.get('password', '')
        form['dob'] = request.POST.get('dob', '')
        form['address'] = request.POST.get('address', '')

        if (DataValidator.is_null(form['first_name'])):
            form['input_error']['first_name'] = 'First Name is required'
            form['input_error']['error'] = True

        if (DataValidator.is_null(form['last_name'])):
            form['input_error']['last_name'] = 'Last Name is required'
            form['input_error']['error'] = True

        if (DataValidator.is_null(form['login_id'])):
            form['input_error']['login_id'] = 'Login ID is required'
            form['input_error']['error'] = True

        if (DataValidator.is_null(form['password'])):
            form['input_error']['password'] = 'Password is required'
            form['input_error']['error'] = True

        if (DataValidator.is_null(form['dob'])):
            form['input_error']['dob'] = 'DOB is required'
            form['input_error']['error'] = True

        if (DataValidator.is_null(form['address'])):
            form['input_error']['address'] = 'Address is required'
            form['input_error']['error'] = True

        if not form['input_error']['error']:
            form['message'] = 'User Registration Sucessfully..!!'

        print('form =', form)

    return render(request, 'registration.html', {'form': form})


def user_signin(request):
    return render(request, 'login.html')