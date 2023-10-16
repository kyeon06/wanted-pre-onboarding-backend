from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError("Members must have an email")
        user = self.model(
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        python manage.py createsuperuwer 사용시 해당 함수 사용
        """

        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class Member(AbstractBaseUser):
    email = models.EmailField("이메일주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    username = models.CharField("이름", max_length=50)
    mobile = models.CharField("휴대폰번호", max_length=20)

    is_active = models.BooleanField("활성화여부", default=True)
    is_admin = models.BooleanField("관리자여부", default=False)

    created_at = models.DateTimeField("생성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간", auto_now=True)

    """ id로 사용 할 필드 지정"""
    USERNAME_FIELD = "email"

    """ custom user 생성시 필요 """
    objects = CustomUserManager()

    def __str__(self):
        return f"email: {self.email} / username: {self.username}"

    def has_perms(self, perm, obj=None):
        """
        - 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
        - admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
        """
        return True

    def has_module_perms(self, app_label):
        """
        - 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
        - admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
        """
        return True

    @property
    def is_staff(self):
        """ admin 권한 설정 """
        return self.is_admin