from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('',views.index,name='index'),
  path('post/<str:pk>',views.post,name='post'),
  path('register',views.register,name='register'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('create_blog',views.create_blog,name='create_blog')
]


if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)