from django.urls import path
from app import views


urlpatterns = [
    
    path('',views.index),
    path("<int:question_id>/",views.details),
    path('<int:question_id>/results/',views.results),
    path('<int:question_id>/votes/',views.votes),
    ]