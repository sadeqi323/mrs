from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('^submit/calin/$',views.submit_calIn, name= 'sub_calin'),
    re_path('^submit/calout/$',views.submit_calOut, name= 'sub_calout'),
]