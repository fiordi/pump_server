from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
  """
  Interface class for User
  """
  username = models.CharField( 'username', max_length=10, unique=True, db_index=True)
  email = models.EmailField('email address', unique=True)
  joined = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'username'

  def __unicode__(self):
    return self.username

