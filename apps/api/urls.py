from django.conf.urls import include, url
from rest_auth import views as rest_auth_views
from rest_framework.routers import DefaultRouter
from apps.api.views.accounts import SignUPView
router = DefaultRouter()


urlpatterns = [
    url('^', include(router.urls)),
]

urlpatterns += [
    url(r'^login/$', rest_auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', rest_auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignUPView.as_view(), name='signup'),
    # Using default view but using custom serializer PasswordResetSerializer
    url(r'^password/reset/$', rest_auth_views.PasswordResetView.as_view(), name='password_reset'),
    # Using default view and serializer
    url(r'^password/reset/confirm/$', rest_auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

