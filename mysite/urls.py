from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views
from mysite.core.views import SearchView

urlpatterns = [
    path('', views.doc_list, name='doc_list'),
    path('docs/upload/', views.upload_doc, name='upload_doc'),
    path('docs/<int:pk>/', views.delete_doc, name='delete_doc'),
    path('admin/', admin.site.urls),
    re_path(r'^category/(?P<category_id>\d+)/$', views.get_by_category, name='category-list'),
    re_path(r'^search/$', views.get_by_serch, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
