# degree_checklist/resources.py

from import_export import resources
from .models import DegreeProgram

class DegreeProgramResource(resources.ModelResource):
    class Meta:
        model = DegreeProgram
        import_id_fields = ('ProgramID','ProgramName','TotalCredits','Department')