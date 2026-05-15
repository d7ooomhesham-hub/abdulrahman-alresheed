
from django.contrib import admin
from .models import Book, Publisher, Author, Address, Student, Gallery # أضف كل الموديلات هنا

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Student)
admin.site.register(Gallery)