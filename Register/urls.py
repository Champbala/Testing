from django.urls import path
from. import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('setcookie',views.setcookie),
    path('showcookie',views.showcookie),
    path('deletecookie',views.delete),
]
