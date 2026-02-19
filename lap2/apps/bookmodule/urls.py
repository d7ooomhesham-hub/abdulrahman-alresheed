from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # للرابط الأول
    path('index2/<int:val1>/', views.index2), # للرابط الثاني (الذي يعمل عندك)
    path('<int:bookId>', views.viewbook), # للرابط الثالث
]