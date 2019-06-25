from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.home,name='homePage'),
    url(r'^search/',views.search,name='search'),
    url(r'^profile/(\d+)',views.profile,name='profile'),
    url(r'^upload$',views.upload,name='upload'),
    url(r'^edit',views.edit,name='edit'),
    url(r'^comment/(\d+)$', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)