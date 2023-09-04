from django.contrib import admin
from django.urls import include,path
urlpatterns = [
    path(&#39;&#39;,include(&#39;member.urls&#39;)),
    path(&#39;admin/&#39;,admin.site.urls),
]
