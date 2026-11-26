from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('register/', views.MyRegistrationView.as_view(), name='register'),
    path('cabinet/', views.PersonalCabinetView.as_view(), name='cabinet'),
    path('cabinet/application/new/', views.ApplicationCreateView.as_view(), name='application_create'),
    path('logout/', LogoutView.as_view(next_page='course_list'), name='logout'),
]