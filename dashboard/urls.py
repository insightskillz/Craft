from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('plagerism/', views.plagerism, name='plagerism'),
    path('content/', views.content, name='content'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
