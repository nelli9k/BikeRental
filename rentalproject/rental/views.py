from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def booking_form(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = BookingForm()
    return render(request, "booking_form.html", {"form": form})

def success(request):
    return render(request, "success.html")