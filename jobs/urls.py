from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('post-job/', views.post_job),

    path('apply/<int:id>/', views.apply_job),

]