from django.urls import path

from . import views

app_name="dpproj"
urlpatterns = [
    path('',views.index, name='index'),
    path('index', views.index, name='index'),
    path('login/',views.login_validation, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('kpi/<str:user>', views.kpi, name='kpi')
]