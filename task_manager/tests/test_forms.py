from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.forms import WorkerCreationForm, TaskForm
from task_manager.models import Position, TaskType, Tag


class FormsTests(TestCase):
    def setUp(self) -> None:
        admin_position = Position(name="Team Lead")
        admin_position.save()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
            position=admin_position,
        )
        self.client.force_login(self.admin_user)

    def test_worker_creation_form_with_position_is_valid(self):
        form_data = {
            "username": "test_user",
            "password1": "test_123",
            "password2": "test_123",
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form.data)
