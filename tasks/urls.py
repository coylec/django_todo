from django.conf.urls import url
from tasks.views import TasksView


urlpatterns = [
    url(r'^$', TasksView.as_view()),
    url(r'(?P<pk>[0-9]+)/$', TasksView.as_view())
]