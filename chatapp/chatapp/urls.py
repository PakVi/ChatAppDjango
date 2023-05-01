from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from chat import views

router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'messages', views.MessageViewSet)


urlpatterns = [
    # path('', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('chat/', include('chat.urls')),
    path('api/', include(router.urls), name='api'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
