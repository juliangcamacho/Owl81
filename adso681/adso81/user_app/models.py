from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name_user = models.CharField(max_length= 20, verbose_name='NOmbre de usuario')
    bio = models.TextField(blank=True,  verbose_name='Biografía')
    phone = models.CharField(null=True, max_length=10, verbose_name='Teléfono')

    def __str__(self):
        return self.name_user

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'
        ordering = ['id']