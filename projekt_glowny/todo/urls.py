from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.tasks_view),
    
    path('api/tasks/<int:id>/done/', views.task_done),
    
    path('api/tasks/<int:id>/', views.task_delete),
]