from django.urls import path
from. import views
urlpatterns = [

    path('view/',views.viewdetails,name='View'),
    path('view/<str:pk>',views.viewiddetails,name='Viewid'),
    path('update/',views.Updatedetails,name='update'),
    path('update/<str:pk>',views.Updatedetailsid,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
]
