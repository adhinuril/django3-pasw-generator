from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request) :
    return render(request,'generator/home.html')

def about(request) :
    return render(request, 'generator/about.html')

def password(request) :
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    default_length = 12
    param_dict = {'upp' : request.GET.get('uppercase'),
                  'spec' : request.GET.get('special'),
                  'num' : request.GET.get('numbers'),
                  'len' : request.GET.get('length'), default_length}

    if param_dict['upp'] :
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if param_dict['spec'] :
        characters.extend(list('!@#$%^&*()'))

    if param_dict['num'] :
        characters.extend(list('1234567890'))

    length = int(param_dict['len'])
    
    thepassword = ''
    
    for x in range(length) :
        thepassword += random.choice(characters)
    param_dict['password'] = thepassword
    return render(request,'generator/password.html', param_dict)
