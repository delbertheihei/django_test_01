from django.urls import path, re_path
from . import views


# namespace
app_name = 'tasks'

urlpatterns = [
    # Create a task
    path('create/', views.task_create, name='task_create'),

    # Retrieve task list
    path('list/', views.task_list, name='task_list'),

    # Retrieve task detail
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

    # Update task
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),

    # Delete task
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
]
