from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager
from django.contrib.gis.db import models




class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    MANAGER = 'manager', 'Manager'
    EMPLOYEE = 'employee', 'Employee'

class CustomUser(AbstractUser):  
    username=None
    email = models.EmailField(unique=True)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    verification_sent_at = models.DateTimeField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone_no = models.CharField(max_length=15,unique=False)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', blank=True)
    location = models.PointField(blank=True, null=True)
