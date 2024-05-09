from django.urls import path
from . import views

urlpatterns = [path('api/vendors/', views.BasicAPI.as_view()),
               path('api/vendors/<int:pk>/',views.SpecificAPI.as_view())]