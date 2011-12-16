# Create your views here.
from django.views.generic import ListView

from models import StudyGroup

class StudyGroupList(ListView):
    model = StudyGroup

    def get_context_data(self, **kwargs):
        return kwargs
