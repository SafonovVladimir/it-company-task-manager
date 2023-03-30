from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Task, Position, TaskType, Tag


class ModelTests(TestCase):
    def setUp(self):
        self.admin_position = Position.objects.create(name="Team Lead")
        self.task_type = TaskType.objects.create(name="Bug")
        self.tag = Tag.objects.create(name="#bug")
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
            position=self.admin_position,
        )
        self.client.force_login(self.admin_user)
        self.task = Task.objects.create(
            name="Name",
            description="Description",
            uploaded="2023-03-29 12:26:16.222495",
            deadline="2023-03-30",
            is_completed=True,
            priority="Urgent",
            task_type=self.task_type,
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), f"{self.task.name}")

    def test_worker_str(self):
        self.assertEqual(
            str(self.admin_user),
            f"{self.admin_user.username} "
            f"({self.admin_user.first_name} {self.admin_user.last_name}, "
            f"{self.admin_user.position})"
        )

    def test_create_worker_with_position(self):
        self.assertEqual(self.admin_user.username, "admin")
        self.assertTrue(self.admin_user.check_password("admin12345"))
        self.assertEqual(self.admin_user.position, self.admin_position)

    def test_tasktype_str(self):
        self.assertEqual(str(self.task_type), f"{self.task.task_type}")
