from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class RoleModel(models.Model):
    id = models.AutoField(primary_key=True)

    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('SELLER', 'Vendedor'),
    )

    name = models.CharField(max_length=10, choices=ROLE_CHOICES, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'roles'


class UserModel(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    role = models.ForeignKey(
        RoleModel,
        on_delete=models.CASCADE,
        related_name='users',
        db_column='role_id',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'password']

    class Meta:
        db_table = 'users'