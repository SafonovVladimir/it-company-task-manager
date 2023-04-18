from django.urls import path

from task_manager.views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerCreateView,
    WorkerDetailView,
    WorkerPositionUpdateView,
    WorkerDeleteView,
    toggle_complete_task,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"
         ),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"
         ),
    path("tasks/<int:pk>/toggle_complete/",
         toggle_complete_task,
         name="toggle-complete-task"
         ),

    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "worker/<int:pk>/update/",
        WorkerPositionUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "worker/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update"
         ),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"
         ),

    path("types/", TaskTypeListView.as_view(), name="type-list"),
    path("types/create/", TaskTypeCreateView.as_view(), name="type-create"),
    path("types/<int:pk>/update/",
         TaskTypeUpdateView.as_view(),
         name="type-update"
         ),
    path("types/<int:pk>/delete/",
         TaskTypeDeleteView.as_view(),
         name="type-delete"
         ),

]

app_name = "task_manager"
