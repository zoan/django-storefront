from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x

# Create your views here.
# request -> response
# request handler
# action
def say_hello(request):
    # pull data from db
    # transform
    # send email
    x = calculate()
    return render(request, 'hello.html', { 'name' : 'Bruh' })