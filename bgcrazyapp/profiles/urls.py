from django.urls import path
from .views import ProfileListView, ProfileDetailView
from profiles import views

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', views.ProfileDetailView, name='detail'),
 
], "profiles")
