from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionMixin
from django.views.decorators.csrf import csrf_exempt


class MyUserManager(BaseUserManager):

	def _create_user(self, username, email, password, **extra_fields):

		if not username:
			raise ValueError('you must have a username')

		user = self.model(
			username=username,
			email = self.normalize_email(email),
			**extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email, password, **extra_fields):

		extra_fields.set_default('is_staff', False)
		return self._create_user(username, email, password, **extra_fields)


	def create_superuser(self, username, email, password, **extra_fields):

		extra_fields.set_default('is_staff', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True')

		return self._create_user(username, email, password, **extra_fields)

class MyUser(AbstractBaseUser):

	username = models.CharField('username', max_length=12, unique=True)
	email = models.EmailField('email', max_length=14,)

	is_staff = models.BooleanField('staff status', default=False)
	is_active = models.BooleanField('active', default=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELD = ['email', ]

	objects = MyUserManager()

	class Meta:
		db_table = 'myuser'

	def __str__(self):
		return self.username

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
#    is_staff check.
	@property
	def is_staff(self):
		return self.is_admin