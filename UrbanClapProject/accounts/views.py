from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
            
    context = {"form": form}
    return render(request, 'registration/register.html', context)

@api_view(['GET',])
def UserView(request):
    user = User.objects.all()
    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)