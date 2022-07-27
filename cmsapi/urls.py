from django.urls import path
from .views import CMSList, CMSDetail,CMSListDetailfilter

app_name = 'cmsapi'

urlpatterns = [
    path('<int:pk>/', CMSDetail.as_view(), name='detailcreate'),
    path('', CMSList.as_view(), name='listcreate'),
    path('search/', CMSListDetailfilter.as_view(), name='postsearch'),
]
