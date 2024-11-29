from django.shortcuts import render

from students.models import Student


def student_list(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    age = request.GET.get('age')
    email = request.GET.get('email')
    if first_name and last_name and age and email:
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email
        )
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student_list.html', ctx)
