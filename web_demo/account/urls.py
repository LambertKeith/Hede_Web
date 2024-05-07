from django.contrib import admin
from django.urls import include, path
from account.views import test_view


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('test/', test_view)
]
