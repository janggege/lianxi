from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^app/', include('app.urls')),
]
