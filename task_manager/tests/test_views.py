from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Task, Position, TaskType, Tag

TASK_URL = reverse("task_manager:task-list")
TASK_URL_WITH_SEARCH = reverse("task_manager:task-list") + "?name=pa"
TAG_URL = reverse("task_manager:tag-list")
TASK_TYPE_URL = reverse("task_manager:type-list")


class PublicTaskTests(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertNotEqual(res.status_code, 200)


class PublicTagTests(TestCase):
    def test_login_required(self):
        res = self.client.get(TAG_URL)
        self.assertNotEqual(res.status_code, 200)


class PublicTaskTypeTests(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_TYPE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivatePositionTests(TestCase):
    def setUp(self):
        task_type1 = TaskType.objects.create(name="Bug")
        task_type2 = TaskType.objects.create(name="New feature")
        task_type3 = TaskType.objects.create(name="Refactoring")
        admin_position = Position.objects.create(name="Team Lead")
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
            position=admin_position,
        )
        task1 = Task.objects.create(
            name="Task1",
            description="Description Task1",
            uploaded="2023-03-29 12:26:16.222495",
            deadline="2023-03-30",
            is_completed=True,
            priority="Urgent",
            task_type=task_type1,
        )
        task2 = Task.objects.create(
            name="Task2",
            description="Description Task2",
            uploaded="2023-03-29 12:26:16.222495",
            deadline="2023-03-30",
            is_completed=True,
            priority="Urgent",
            task_type=task_type2,
        )
        task3 = Task.objects.create(
            name="Task2",
            description="Description Task2",
            uploaded="2023-03-29 12:26:16.222495",
            deadline="2023-03-30",
            is_completed=True,
            priority="Urgent",
            task_type=task_type3,
        )

    def test_retrieve_task(self):
        response = self.client.get(TASK_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(
                response.context["task_list"]
            ), list(tasks)
        )
        self.assertTemplateUsed(response, "task_manager/task_list.html")

    def test_retrieve_task_with_search(self):
        response = self.client.get(TASK_URL_WITH_SEARCH)

        tasks = Task.objects.filter(name__icontains="pa")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "task_manager/task_list.html")
