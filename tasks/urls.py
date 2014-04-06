from django.conf.urls import patterns, include, url

from .views import (ListTasksView, CreateTaskView, DetailTaskView,
    UpdateTaskView, SetTaskReadyView, SetTaskIncompleteView, SetTaskCompletedView)

urlpatterns = patterns('',
    url(r'^$', ListTasksView.as_view(), name='list_tasks'),
    url(r'^create/$', CreateTaskView.as_view(), name='create_task'),
    url(r'^(?P<pk>\d+)/$', DetailTaskView.as_view(), name='task_detail'),
    url(r'^(?P<pk>\d+)/edit/$', UpdateTaskView.as_view(), name='edit_task'),
    url(r'^(?P<pk>\d+)/incomplete/$',
        SetTaskIncompleteView.as_view(),
        name='set_task_incomplete'),
    url(r'^(?P<pk>\d+)/ready/$',
        SetTaskReadyView.as_view(),
        name='set_task_ready'),
    url(r'^(?P<pk>\d+)/complete/$',
        SetTaskCompletedView.as_view(),
        name='set_task_complete'),
)
