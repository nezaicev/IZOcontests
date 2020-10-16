from django.contrib.auth.models import BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self,email,password):
        user=self.model(email=email,password=password)
        user.set_password(password)
        user.is_staff=False
        user.is_superuser=False
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user=self.model(email=email,password=password)
        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)