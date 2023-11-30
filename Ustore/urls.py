from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

admin.site.site_header = 'Uncanny Store Backdoor'                    # default: "Django Administration"
admin.site.index_title = 'Settings'                 # default: "Site administration"
admin.site.site_title = 'Staff Room' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
