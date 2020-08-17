from django.urls import path

from . import views
app_name="kpi"
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/result/
    path('<int:question_id>/result/', views.result, name='result'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]