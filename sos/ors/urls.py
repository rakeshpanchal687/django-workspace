from django.urls import path
from . import views, views_new

urlpatterns = [
    path('', views_new.welcome),
    path('welcome/', views_new.welcome),
    path('signup/', views.user_signup),
    path('signin/', views_new.user_signin),
    path('logout/', views_new.user_logout),
    path('testlist/', views_new.test_list),
    path('list/', views_new.user_list),
    path('delete/<int:id>/', views_new.delete_user),
    path('save/', views_new.user_save),
    path('save/<int:id>/', views_new.user_save),

]
