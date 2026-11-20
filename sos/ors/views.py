from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.user_service import UserService
from .utility.data_validator import DataValidator


def test_ors(request):
    return HttpResponse('<h1>ORS APP</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}
    form['input_error']['error'] = False

    if request.method == "GET":
        return render(request, 'registration.html', {'form': form})

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

        if form['input_error']['error']:
            return render(request, 'registration.html', {'form': form})

        try:
            UserService().add(form)
            form['error'] = False
            form['message'] = 'User Registration Sucessfully..!!'
        except Exception as e:
            form['error'] = True
            form['message'] = str(e)

        # print('form =', form)

        return render(request, 'registration.html', {'form': form})


def user_signin(request):
    form = {}
    form['message'] = ''
    form['input_error'] = {}
    form['input_error']['error'] = False

    if request.method == "GET":
        return render(request, 'login.html', {'form': form})

    if request.method == "POST":
        form['login_id'] = request.POST.get('loginId', '')
        form['password'] = request.POST.get('password', '')

        if (DataValidator.is_null(form['login_id'])):
            form['input_error']['login_id'] = 'Login ID is required'
            form['input_error']['error'] = True

        if (DataValidator.is_null(form['password'])):
            form['input_error']['password'] = 'password is required'
            form['input_error']['error'] = True

        if form['input_error']['error']:
            return render(request, 'login.html', {'form': form})

        user_list = UserService().authenticate(form['login_id'], form['password'])

        if user_list:
            request.session['first_name'] = user_list[0].get('first_name')
            # return render(request, 'welcome.html', {'first_name': user_list[0].get('first_name')})
            return redirect('/ors/welcome/')
        else:
            form['error'] = True
            form['message'] = 'Login ID & Password Invalid'
            # form['message'] = 'User Login Sucessfully..!!'

        # print('form =', form)

        return render(request, 'login.html', {'form': form})


def user_logout(request):
    request.session['first_name'] = None
    request.session.flush()
    return redirect('/ors/signin/')
