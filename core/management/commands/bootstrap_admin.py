import os

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.password_validation import validate_password


class Command(BaseCommand):
    help = 'Create or reset a superuser from temporary deployment environment variables'

    def handle(self, *args, **options):
        username = os.environ.get('BOOTSTRAP_ADMIN_USERNAME')
        password = os.environ.get('BOOTSTRAP_ADMIN_PASSWORD')

        if not username and not password:
            self.stdout.write('Admin bootstrap skipped; no credentials were provided.')
            return
        if not username or not password:
            raise CommandError(
                'Both BOOTSTRAP_ADMIN_USERNAME and BOOTSTRAP_ADMIN_PASSWORD are required.'
            )

        User = get_user_model()
        user = User._default_manager.filter(
            **{User.USERNAME_FIELD: username}
        ).first()

        if user and not user.is_superuser:
            raise CommandError(
                'The requested username belongs to a non-superuser; choose another username.'
            )

        candidate = user or User(**{User.USERNAME_FIELD: username})
        try:
            validate_password(password, user=candidate)
        except ValidationError as exc:
            raise CommandError('The supplied password does not meet the password policy.') from exc

        if user:
            user.set_password(password)
            user.save(update_fields=['password'])
            action = 'reset'
        else:
            User._default_manager.create_superuser(
                **{User.USERNAME_FIELD: username},
                password=password,
            )
            action = 'created'

        self.stdout.write(self.style.SUCCESS(f'Superuser {action}; password was not logged.'))
