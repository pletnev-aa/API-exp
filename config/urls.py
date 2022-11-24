from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import include, path
from rest_framework import routers

from callback.views import BillingViewSet, UploadFile

router = routers.DefaultRouter()
router.register(r'api/upload_csv', UploadFile, basename="upload")
router.register(r'api/invoices', BillingViewSet, basename='invoices')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static('static/', views.serve)
