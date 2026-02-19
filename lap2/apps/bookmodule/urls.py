from django.urls import path
from . import views # استيراد ملف views الموجود في نفس المجلد [cite: 132, 133]

urlpatterns = [
    path('', views.index), # المهمة 1 و 2 [cite: 136]
    path('index2/<int:val1>/', views.index2), # المهمة 3 [cite: 138]
    path('<int:bookId>', views.viewbook), # المهمة 7 [cite: 167]
]