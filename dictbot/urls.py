from django.conf.urls import patterns, include, url
from django.contrib import admin
from main_app.views import dictbot
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dictbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shaurya/?$', dictbot.as_view())
)
