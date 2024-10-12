from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def book_a_bike(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.bike = bike
            booking.save()
            return redirect('success')
    else:
        form = BookingForm(initial={'bike': bike})

    return render(request, 'book_a_bike.html', {'form': form, 'bike': bike})

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

def contacts(request):
    staff = [
        {"name": "John Doe", "position": "Manager", "email": "john.doe@example.com", "phone": "+1 123 456 7890"},
        {"name": "Jane Smith", "position": "Customer Support", "email": "jane.smith@example.com", "phone": "+1 987 654 3210"},
        {"name": "Emily Johnson", "position": "Technician", "email": "emily.johnson@example.com", "phone": "+1 555 555 5555"},
    ]
    return render(request, 'contacts.html', {'staff': staff})   

@login_required
def protected_view(request):
    return render(request, 'protected.html')