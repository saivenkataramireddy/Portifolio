from django.contrib import admin
from django.urls import path
from demoapp import views  # ✅ import views from your app
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("project/<str:project_id>/", views.project_detail, name="project_detail"),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
