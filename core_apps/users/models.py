import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_('first name'), max_length=50)
    last_name = models.CharField(verbose_name=_('last name'), max_length=50)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'
        ordering = ('-date_joined',)

    def __str__(self) -> str:
        return self.get_full_name

    @property
    def get_full_name(self) -> str:
        return f'{self.first_name.title()} {self.last_name.title()}'

    @property
    def get_short_name(self) -> str:
        return self.first_name
