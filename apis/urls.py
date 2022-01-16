from django.urls import include, path,re_path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('listfolders',views.folder_names, name="folders"),
    path('listdocuments',views.listdocuments, name="documents"),
    path('listtopics',views.listtopics, name="topics"),
    re_path(r'^listdocuments/(?P<folder>[\w ]+\w{0,50})/$',view=views.listdocuments, name="documents"),
    path('createfolder',views.create_folder,name="CreateFolder"),
    path('createdocument',views.create_document,name="CreateDocument"),
    path('createtopics',views.create_topic,name="CreateTopic"),
    path('uploadfile',views.uploadfile,name="Uploadfile"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]