from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError

from .managers import CustomUserManager

game_types = (
    ('S', "Singles"),
    ('D', "Doubles"),
    ('MD', "Mixed Doubles"),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    gender = (
        ('F', "Female"),
        ('M', "Male"),
        ('NB', "Non-binary"),
    )
    email = models.EmailField(_('email address'), unique=True)
    level = models.DecimalField(max_digits=2, decimal_places=1)
    gender = models.CharField(max_length=2, choices=gender)
    singles = models.BooleanField()
    doubles = models.BooleanField()
    mixed_doubles = models.BooleanField()
    picture = models.CharField(max_length=1000, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Match(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    match = models.ManyToManyField(CustomUser)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='match_created_by')
    created_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=game_types)

    def clean(self, *args, **kwargs):
        if self.users.count() == 2 or self.users.count == 4:
            raise ValidationError("You can't assign more than four users to doubles group.")


class Message(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    text = models.TextField()
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='message_match')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='message_created_by')
    created_date = models.DateTimeField(default=timezone.now)

