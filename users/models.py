from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина')
    )

    middle_name = models.CharField('Middle name', max_length=45, default='')
    gender = models.CharField('Пол', max_length=1, choices=GENDERS)
    photo = models.ImageField('Аватар', upload_to='img/')
