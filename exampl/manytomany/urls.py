from django.conf.urls.defaults import patterns, url

from views import StudyGroupList

urlpatterns = patterns('',
    url('^list/$', StudyGroupList.as_view()),
)
