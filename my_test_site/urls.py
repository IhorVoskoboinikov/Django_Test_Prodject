from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from crm.views import first_page, thanks_page

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', first_page),
                  path('thanks/', thanks_page, name='thanks'),
              ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)