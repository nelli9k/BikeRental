from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking_form, name="booking_form"),
    path('book/<int:bike_id>/', views.book_a_bike, name='book_a_bike'),
    path("contacts/", views.contacts, name="contacts"),
    path("success/", views.success, name="success"),
    path("protected/", views.protected_view, name="protected_view"), 
]
