
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views as account_views


admin.site.site_header = 'Django Blog'
admin.site.site_title = 'Welcome to the Django Blog'
admin.site.index_title = 'Welcome to this Portal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register', account_views.register, name= 'register'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'logout.html'), name= 'logout'),
    path('login', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('profile', account_views.profile, name= 'profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)