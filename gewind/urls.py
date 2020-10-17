from django.urls import path
from . import views

app_name='gewind'

urlpatterns=[
    path('about/', views.About.as_view(), name='about'),
    path('example/', views.UploadfileList.as_view(), name='example'),
    path('howto/', views.Howto.as_view(), name='howto'),
    path('', views.Top.as_view(), name='top'),
    path('make/', views.ProjectInfoFormsetView.as_view(), name='make'),
    path('make/dl/<str:slug>/',views.dl,name='dl'),

    # ----ToDo: Check----
    # path('test/thanks/<str:slug>/',views.Thanks.as_view(),name='thanks'),
    # ----ToDo: Check----
    # path('coordinatesinput/',views.index,name='coordinates_input'),
]