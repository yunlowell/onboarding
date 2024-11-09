from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=10, unique=True)
    
    USER = 'USER'
    ADMIN = 'ADMIN'
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
    ]
    roles = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

    def __str__(self):
        return self.username

    # username 필드 수정
    username_validator = RegexValidator(
                regex=r'^[\w\s]+$',  # 공백 포함 유효성 검사
                message="Username은 영어, 숫자, 공백만 허용됩니다."
    )

    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[username_validator]
    )