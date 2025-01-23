from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from django_registration.backends.one_step.views import RegistrationView

from django.urls import reverse_lazy

from core.views import IndexTemplateView
from users.forms import CustomUserForm

from django.views.static import serve




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',
        RegistrationView.as_view(form_class=CustomUserForm, success_url='/raceChoose/'),
        name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path("api-auth/", include("rest_framework.urls")),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/v1/', include('api.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="spa-entry-point"),


]
