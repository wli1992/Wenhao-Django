# views.py

from django.shortcuts import render, redirect
from .forms import DegreeProgramForm, CourseForm,DegreeProgram, Course

def create_degree_program(request):
    if request.method == 'POST':
        form = DegreeProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('degree_program_list')
    else:
        form = DegreeProgramForm()

    return render(request, 'create_degree_program.html', {'form': form})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'create_course.html', {'form': form})

def degree_program_list(request):
    degree_programs = DegreeProgram.objects.all()
    return render(request, 'degree_program_list.html', {'degree_programs': degree_programs})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


# def model_list(request):
#     degree_programs = DegreeProgram.objects.all()
#     courses = Course.objects.all()

#     context = {
#         'degree_programs': degree_programs,
#         'courses': courses,
#     }

#     return render(request, 'model_list.html', context)


def model_list(request):
    # Determine the model type based on the URL
    model_type = request.path.split('/')[-2]  # Extract the second-to-last part of the URL
    
    # Get the 'sort' parameter from the URL
    sort_param = request.GET.get('sort', 'name')  # Default sorting by 'name'

    # Use the model type to fetch the corresponding queryset
    if model_type == 'degree_program_list':
        objects = DegreeProgram.objects.all()

        # Handle numeric sorting separately
        if sort_param in ['TotalCredits']:
            objects = sorted(objects, key=lambda x: int(getattr(x, sort_param)))
        else:
            objects = objects.order_by(sort_param)

    elif model_type == 'course_list':
        objects = Course.objects.all().order_by(sort_param)
    else:
        # Handle other model types or provide a default queryset
        objects = []

    print("Sorted Objects:", objects)

    return render(request, 'model_list.html', {'degree_programs': objects, 'sort_param': sort_param, 'model_type': model_type})