<<<<<<< HEAD

from django.shortcuts import render
from django.http import HttpResponse

# المهمة 1 و 2: استقبال الاسم من الرابط
def index(request):
    name = request.GET.get("name") or "world!" # [cite: 60]
    return render(request, "bookmodule/index.html", {"name": name}) # [cite: 121]

# المهمة 3: استقبال متغير من مسار الرابط
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1)) # [cite: 73]
def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = book1 if book1['id'] == bookId else (book2 if book2['id'] == bookId else None)
    return render(request, 'bookmodule/index.html', {'book': targetBook}) # [cite: 159]

=======
from django.shortcuts import render

# Create your views here.
>>>>>>> origin/main
