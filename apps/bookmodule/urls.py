from django.urls import path
from . import views

# ضروري جداً لربط الروابط بكلمة books:
app_name = 'books'

urlpatterns = [
    # --- 1. الروابط الأساسية ---
    path('', views.index, name='index'),
    path('list_books/', views.list_books, name='list_books'),
    path('<int:bookId>/', views.viewbook, name='view_one_book'),
    path('aboutus/', views.aboutus, name='aboutus'),
    
    # --- 2. Lab 12: نظام المستخدمين والرسائل (Tasks 1, 2, 4) ---
    # رابط التسجيل [cite: 12]
    path('users/register', views.register_user, name='register'),
    # رابط تسجيل الدخول [cite: 13]
    path('users/login', views.login_user, name='login'),
    # رابط تسجيل الخروج [cite: 15]
    path('users/logout', views.logout_user, name='logout'),
    
    # --- 3. Lab 11: الطلاب والصور (Tasks 1, 3) ---
    # رابط إدارة الطلاب والعناوين (علاقة Many-to-Many) [cite: 29, 30]
    path('lab11/addstudent/', views.add_student, name='add_student'),
    # رابط معرض الصور ومعالجتها [cite: 33]
    path('lab11/gallery/', views.add_to_gallery, name='add_to_gallery'),

    # --- 4. Lab 10: CRUD Operations (Part 1 & 2) ---
    # الجزء الأول: بدون Django Forms
    path('lab10/part1/listbooks', views.lab10_listbooks, name='lab10_listbooks'),
    path('lab10/part1/addbook', views.lab10_addbook, name='lab10_addbook'),
    path('lab10/part1/editbook/<int:id>', views.lab10_editbook, name='lab10_editbook'),
    path('lab10/part1/deletebook/<int:id>', views.lab10_deletebook, name='lab10_deletebook'),

    # الجزء الثاني: باستخدام Django Forms [cite: 22]
    path('lab10/part2/listbooks', views.lab10_part2_listbooks, name='lab10_part2_listbooks'),
    path('lab10/part2/addbook', views.lab10_part2_addbook, name='lab10_part2_addbook'),
    path('lab10/part2/editbook/<int:id>', views.lab10_part2_editbook, name='lab10_part2_editbook'),
    path('lab10/part2/deletebook/<int:id>', views.lab10_part2_deletebook, name='lab10_part2_deletebook'),

    # --- 5. روابط Lab 9 (إحصائيات وقاعدة البيانات) ---
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'),
    path('add-lab9-data/', views.add_lab9_data, name='add_lab9_data'),
]