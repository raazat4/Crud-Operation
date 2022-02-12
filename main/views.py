from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import AddStudentForm
# Create your views here.


class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'main/home.html', {'studata':stu_data})
    
class Add_Student(View):
    def get(self, request):
        form = AddStudentForm()
        return render(request, 'main/add_student.html', {'form':form})
    
    def post(self, request):
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
        else:
            return render(request, 'main/add_student.html', {'form':form})

class Destroy_Student(View):
    def post(self, request):
                data = request.POST
                id = data.get('id')
                studata = Student.objects.get(id=id)
                studata.delete()
                return redirect('/')
            
class Edit_Student(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        form = AddStudentForm(instance=stu)
        return render(request, 'main/edit_student.html',{'form':form})
    def post(self, request, id):
        stu = Student.objects.get(id=id)
        form = AddStudentForm(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            return redirect('/')