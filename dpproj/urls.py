from django.urls import path

from . import views

app_name="dpproj"
urlpatterns = [
    path('',views.index, name='index'),
    path('index', views.index, name='index'),
    path('login/',views.login_validation, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('kpi/<str:user>', views.kpi, name='kpi'),
    path('kpi/registration/<str:user>', views.kpi_registration, name='registration'),
    path('kpi/registration/complete/<str:user>',views.kpi_registration_complete,name='complete'),
    path('kpi/upload/<str:user>', views.kpi_upload, name='upload'),
    path('kpi/visualiation/<str:user>',views.get_visualization, name='visual')
]