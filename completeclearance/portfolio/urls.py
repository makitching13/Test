from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    # ex: /portfolio/
    path('', views.index, name='index'),
    # ex: /portfolio/5/
    path('<int:project_id>/', views.detail, name='detail'),
]
