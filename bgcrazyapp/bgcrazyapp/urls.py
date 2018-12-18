from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from django.conf.urls.static import static
from profiles import views as profiles_views


from messenger.urls import messenger_patterns

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
 

    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de Messenger
    path('direct/', include(messenger_patterns)),

    path('follows', profiles_views.Follow_user, name='follow_user'),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)