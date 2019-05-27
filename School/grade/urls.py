from django.conf.urls import url

from .views import GradeListView

urlpatterns = [
    url(r'^$', GradeListView.as_view(), name='gradelist'),
]