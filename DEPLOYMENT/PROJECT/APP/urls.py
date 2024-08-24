from django.urls import path
from . import views

urlpatterns =[
    
    path('', views.Home1, name='Home1'),
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('Info/', views.Info, name='Info'),
    path('Deploy/', views.Deploy, name='Deploy'),
    path('Home2', views.Home2, name='Home2'),
    path('Problem_Statement/', views.Problem_Statement, name='Problem_Statement'),
    path('Team/', views.Team, name='Team'),
    path('Result/', views.Result, name='Result'),
    path('Database1/', views.Database1, name='Database1'),
    path('Database2/', views.Database2, name='Database2'),
]