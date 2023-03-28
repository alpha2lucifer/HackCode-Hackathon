from django.urls import path
from api import views

urlpatterns = [
    path('Udata/', views.userlist.as_view()),
]