from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup, name = 'user-signup'),
    path('login/',views.loginPage, name = 'user-login'),
    path('logout/',views.logoutUser, name = 'user-logout'),

    path('',views.index, name = 'home'),

    path('upload/',views.upload, name='user-upload'),
    path('delete/<int:pk>/',views.delete_file, name = 'file-delete'),
    path('student/',views.student, name = 'user-student'),
] 