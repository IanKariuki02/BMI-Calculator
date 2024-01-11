from django.urls import path
from . import views  # Assuming views reside in the same directory

urlpatterns = [
    path('', views.bmi_calculator, name='bmi_calculator'),  # Example pattern
    # Add other patterns as needed
]
