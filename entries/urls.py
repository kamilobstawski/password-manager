from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'get-entry/(?P<pk>[0-9]+)/$', views.EntryView.as_view(), name='get_entry'),
    url(r'entries/$', views.ListEntryView.as_view(), name='entries'),
    url(r'create-entry/$', views.CreateEntryView.as_view(), name='create_entry'),
    url(r'update-entry/(?P<pk>[0-9]+)/$', views.UpdateEntryView.as_view(), name='update_entry'),
    url(r'delete-entry/(?P<pk>[0-9]+)/$', views.DeleteEntryView.as_view(), name='delete_entry'),
    url(r'generate-link/(?P<entry_pk>[0-9]+)/$', views.GenerateLink.as_view(), name='generate_link'),
    url(r'temporary-entry/(?P<token>\w+)/$', views.TemporaryEntryView.as_view(), name='temporary_entry'),
]
