from django.urls import path
from .views import Home, Add_Student, Destroy_Student, Edit_Student

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('add_student/', Add_Student.as_view(), name='add_student'),
    path('destroy_student/', Destroy_Student.as_view(), name='destroy_student'),
    path('edit_student/<int:id>/', Edit_Student.as_view(), name='edit_student')
]