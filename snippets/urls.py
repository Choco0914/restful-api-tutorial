# snippets url을 정의한다.
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from snippets import views

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    re_path(r'^$', views.api_root),
    re_path(r'^schema/', schema_view),
    re_path(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    re_path(r'^snippets/(?P<pk>\w+)/$', views.SnippetDetail.as_view(),
        name='snippet-detail'),
    re_path(r'^snippets/(?P<pk>\w+)/highlight/$',
        views.SnippetHighlight.as_view(), name='snippet-highlight'),
    re_path(r'users/', views.UserList.as_view(), name='user-list'),
    re_path(r'users/(?P<pk>\w+)/$', views.UserDetail.as_view(),
        name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
