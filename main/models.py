from django.db import models
from users.models import CustomUser


class Theme(models.Model):
    name = models.CharField('name', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Link(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    button_text = models.CharField(max_length=25)
    link_address = models.CharField(max_length=200)
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.button_text

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
