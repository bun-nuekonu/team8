from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('username must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser')

        return self._create_user(username, password)


# Usersテーブル
class Users(AbstractUser):
    objects = CustomUserManager()

    def __str__(self):
        return self.username


# Quizzesテーブル
class Quizzes(models.Model):
    quiz = models.TextField(null=False)
    choice1_answer = models.TextField(null=False)
    choice2 = models.TextField(null=False)
    choice3 = models.TextField(null=False)
    choice4 = models.TextField(null=False)


# Timesテーブル
class Times(models.Model):
    time = models.TextField(null=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    
