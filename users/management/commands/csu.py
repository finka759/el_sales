
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@a.com',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('admin')
        user.save()
