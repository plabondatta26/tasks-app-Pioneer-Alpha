from django.urls import path

from .views import DirectoryCreateAPiView, DirectoryListAPIView, DirectoryUpdateAPiView, DirectoryDestroyAPIView,\
    TaskCreateAPIView, TaskListApiView, TaskUpdateAPIView, ChangeTaskStatusAPIView, TaskDeleteAPIView

urlpatterns = [
    # directory
    path('create/deractory/', DirectoryCreateAPiView.as_view(), name='create_directory'),
    path('all/deractory/', DirectoryListAPIView.as_view(), name='all_directory'),
    path('edit/deractory/', DirectoryUpdateAPiView.as_view(), name='edit_directory'),
    path('delete/deractory/', DirectoryDestroyAPIView.as_view(), name='delete_directory'),

    # task
    path('create/task/', TaskCreateAPIView.as_view(), name='create_task'),
    path('all/task/', TaskListApiView.as_view(), name='all_task'),
    path('edit/task/<int:pk>/', TaskUpdateAPIView.as_view(), name='update_task'),
    path('edit/task/status/<int:pk>/', ChangeTaskStatusAPIView.as_view(), name='change_task_status'),
    path('delete/task/<int:pk>/', TaskDeleteAPIView.as_view(), name='delete_task'),
]
