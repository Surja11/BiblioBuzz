from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
  def create_user(self, email, password = None,**extra_fields):
    if not email:
      raise ValueError("User must have a valid email")
    
    user = self.model(email = self.normalize_email(email),**extra_fields)
    user.set_password(password)
    user.save(using = self._db)
    return user
  
  def create_superuser(self, email, password = None,**extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff = True')
    
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser = True')
    

    user = self.create_user(email, password,**extra_fields)
    user.is_staff = True
    user.is_superuser =True
    user.save(using = self._db )
    return user


class User(AbstractBaseUser):
  email = models.EmailField(unique = True)
  username = models.CharField(max_length = 255)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS =['username']
  objects = UserManager()
  
  def __str__(self):
    return self.username
  
  def has_perm(self, perm, obj = None):
    return self.is_superuser
  
  def has_module_perms(self, app_label):
    return self.is_superuser