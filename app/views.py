from django.shortcuts import render

# Create your views here.
def firstbootstrap(request):
    return render(request,'firstbootstrap.html')


def signup(request):
    return render(request,'signup.html')


def signin(request):
    return render(request,'signin.html')