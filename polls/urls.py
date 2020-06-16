from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('analysis/', views.analysis),
    path('fileUpload/', views.upload),

]
