from itertools import groupby
from django.views.generic import ListView
from models import StudyGroup


class StudyGroupList(ListView):
    model = StudyGroup

    def get_context_data(self, **kwargs):
        studygroup_list = kwargs['object_list']
        studygroup_users = StudyGroup.users.through.objects
        studygroup_users = studygroup_users.filter(
                studygroup__in=studygroup_list)
        studygroup_users = studygroup_users.select_related('user')
        studygroup_users = studygroup_users.order_by('studygroup')
        grouped_users = {}
        for k, g in groupby(studygroup_users, lambda o: o.studygroup_id):
            grouped_users[k] = list(g)
        for sg in studygroup_list:
            sg.studygroup_users = grouped_users.pop(sg.id, [])
        return kwargs
