from django.urls import path
from . import views

app_name = 'eval'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<int:item_id>/', views.audio_list, name='audio_list'),
]