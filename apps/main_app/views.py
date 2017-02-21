from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    context = {
        'emails': Email.objects.all(),
        'last_email': Email.objects.last()
    }
    return render(request, 'main_app/index.html', context)

def create(request):

    if request.method == 'POST':

        errors = []

        if not request.POST['email']:
            errors.append('Email field is required')
        if not EMAIL_REGEX.match(request.POST['email']):
            errors.append('Please enter a valid email')

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            email = Email.objects.create(email=request.POST['email'])
            print email

    return redirect('index')
