from django import forms
from .models import Book, Student, Address, Gallery

# فورم الكتاب (Lab 10)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'rating']

# فورم الطالب - علاقة Many-to-Many (Lab 11 - Task 1 & 2)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'addresses']
    
    # حقل اختيار العناوين المتعددة باستخدام Checkboxes 
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

# فورم معرض الصور (Lab 11 - Task 3)
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']