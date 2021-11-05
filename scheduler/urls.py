from django.urls import path

from scheduler import views

urlpatterns = [
    path('timeslot/', views.TimeSlotView.as_view(), name="timeslot"),
    path('available-timeslot/', views.AvailableTimeSlotView.as_view(), name="available-timeslot")
]
