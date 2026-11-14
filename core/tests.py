import os
from io import StringIO
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.management import call_command, CommandError
from django.test import TestCase


class BootstrapAdminCommandTests(TestCase):
    def call_bootstrap(self, username=None, password=None):
        env = {}
        if username is not None:
            env['BOOTSTRAP_ADMIN_USERNAME'] = username
        if password is not None:
            env['BOOTSTRAP_ADMIN_PASSWORD'] = password

        output = StringIO()
        with patch.dict(os.environ, env, clear=True):
            call_command('bootstrap_admin', stdout=output)
        return output.getvalue()

    def test_missing_credentials_are_a_no_op(self):
        output = self.call_bootstrap()
        self.assertIn('skipped', output)
        self.assertFalse(get_user_model().objects.exists())

    def test_creates_superuser_without_logging_password(self):
        password = 'R3liable-unique-passphrase-2026!'
        output = self.call_bootstrap('site-admin', password)
        user = get_user_model().objects.get(username='site-admin')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password(password))
        self.assertNotIn(password, output)

    def test_resets_existing_superuser_password(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='existing-admin',
            email='admin@example.com',
            password='Old-strong-passphrase-2026!',
        )
        new_password = 'N3w-unique-passphrase-2026!'

        self.call_bootstrap('existing-admin', new_password)

        user.refresh_from_db()
        self.assertTrue(user.check_password(new_password))

    def test_refuses_to_promote_existing_regular_user(self):
        User = get_user_model()
        User.objects.create_user(username='ordinary-user', password='Existing-pass-2026!')

        with self.assertRaisesMessage(CommandError, 'belongs to a non-superuser'):
            self.call_bootstrap('ordinary-user', 'Another-unique-pass-2026!')

    def test_requires_both_credentials(self):
        with self.assertRaisesMessage(CommandError, 'Both BOOTSTRAP_ADMIN_USERNAME'):
            self.call_bootstrap(username='site-admin')

    def test_rejects_weak_password(self):
        with self.assertRaisesMessage(CommandError, 'does not meet the password policy'):
            self.call_bootstrap('site-admin', 'password')