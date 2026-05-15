from django.db import models
from django.contrib.auth.models import User # مطلوب لـ Lab 12 [cite: 5, 12]

# --- 1. جداول Lab 9 و Lab 10 ---

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    def __str__(self): return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    def __str__(self): return self.name

class Book(models.Model): # تأكد من وجود هذا الكلاس ليختفي خطأ الـ ImportError
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)
    def __str__(self): return self.title

# --- 2. جداول Lab 11 (Many-to-Many & Images) ---

class Address(models.Model): # [cite: 26, 29]
    city = models.CharField(max_length=100)
    def __str__(self): return self.city

class Student(models.Model): # [cite: 26, 29]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Task 2: تحويل العلاقة إلى Many-to-Many [cite: 30, 31]
    addresses = models.ManyToManyField(Address) 
    def __str__(self): return self.name

class Gallery(models.Model): # Task 3: جدول الصور 
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/') # يتطلب مكتبة Pillow [cite: 33, 34]
    def __str__(self): return self.title