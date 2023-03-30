from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        admin_position = Position(name="Team Lead")
        admin_position.save()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
            position=admin_position,
        )
        self.client.force_login(self.admin_user)
        worker_position = Position(name="Developer")
        worker_position.save()
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="worker12345",
            position=worker_position,
        )

    def test_worker_position_listed(self):
        """Test that worker's position is in list_display
        on driver admin page"""
        url = reverse("admin:task_manager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)

    def test_worker_detailed_position_listed(self):
        """Test that driver's license number is in driver detail admin page"""
        url = reverse(
            "admin:task_manager_worker_change",
            args=[self.worker.pk]
        )
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
