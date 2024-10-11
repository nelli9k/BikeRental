from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Bike

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def booking_form(request):
    bikes = Bike.objects.all()
    return render(request, 'booking_form.html', {'bikes': bikes})

# def booking_form(request):
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, "success.html")
#     else:
#         form = BookingForm()

#     return render(request, "booking_form.html", {"form": form})

def success(request):
    return render(request, "success.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def protected_view(request):
    return render(request, 'protected.html')