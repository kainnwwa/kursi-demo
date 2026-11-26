from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

class UserWithPhone(AbstractUser):
    phone = models.CharField(
        "Номер телефона",
        max_length=17,
        validators=[
        RegexValidator (r'^\+?8?\(?9\d{2}\)?\s?\d{3}-?\d{2}-?\d{2}$',
                message="Формат: +7(999) 123-45-67 или 89991234567")
        ]
    )

User = get_user_model()

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='courses/', blank=True, null=True)
    duration = models.CharField('Длительность', max_length=50, default='Не указана')

    def __str__(self):
        return self.name

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Курс")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.user.username} - {self.service.name}"