# degree_checklist/models.py

# from django.db import models
# from django.apps import apps
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from import_export import resources
# from .models import DegreeProgram
from django.db import models
from django.apps import apps


class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=255)

    def __str__(self):
        return self.DepartmentName


class DegreeProgram(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    ProgramName = models.CharField(max_length=255)
    TotalCredits = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProgramName


class CoreRequirement(models.Model):
    RequirementID = models.AutoField(primary_key=True)
    RequirementName = models.CharField(max_length=255)

    def __str__(self):
        return self.RequirementName


class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=255)
    Credits = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseName


class DegreespecificRequirement(models.Model):
    DegreespecificReqID = models.AutoField(primary_key=True)
    DegreespecificReqName = models.CharField(max_length=255)

    def __str__(self):
        return self.DegreespecificReqName


class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"


class EnrollsIn(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} enrolls in {self.degree_program}"


class BelongsTo(models.Model):
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.degree_program} belongs to {self.department}"


class Requires(models.Model):
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    core_requirement = models.ForeignKey(CoreRequirement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.degree_program} requires {self.core_requirement}"


class Includes(models.Model):
    core_requirement = models.ForeignKey(CoreRequirement, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.core_requirement} includes {self.course}"


class Has(models.Model):
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    Degreespecific_requirement = models.ForeignKey(DegreespecificRequirement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.degree_program} has {self.Degreespecific_requirement}"


class IncludesDegreespecific(models.Model):
    Degreespecific_requirement = models.ForeignKey(DegreespecificRequirement, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Degreespecific_requirement} includes {self.course}"

# class DegreeProgramResource(resources.ModelResource):
#     class Meta:
#         model = DegreeProgram

# class DegreeProgramAdmin(ImportExportModelAdmin):
#     resource_class = DegreeProgramResource