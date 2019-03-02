"""book_sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from book import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
   password_reset, 
   password_reset_done,
   password_reset_confirm,
   password_reset_complete,
   password_change,
   password_change_done,
)

urlpatterns = [

	# the new password reset URLs
    url(r'^accounts/password/reset/$', 
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', 
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^accounts/password/change/$', password_change, {
        'template_name': 'registration/password_change_form.html'}, 
        name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done, 
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),

       
	#url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
	#\d{1,2} \d 表示一個數字, 而 {1,2} 表示 1 到 2 位數
	#\d+ 後面跟1個或更多數字
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.home,name='home'),
	url(r'^catalog/(?P<pk>\d{1,2})/$', views.catalog, name='catalog'),
	url(r'^book/(?P<book_id>\d{1,2})/$', views.book_detail, name='book_detail'),
	url(r'^book/(?P<book_id>\d{1,2})/comment/$', views.add_rating, name='add_rating'),
	url(r'^book/(?P<book_id>\d{1,2})/comment/(?P<comment_id>\d{1,2})$', views.commentLikes, name='commentLikes'),
	url(r'^profile/(?P<username>\d{1,2})/$', views.profile, name='profile'),
	url(r'^profile/edit/$', views.editProfile, name='editProfile' ),

	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	#url(r'^accounts/', include('allauth.urls')),
	
	url(r'^accounts/login/$', auth_views.login), 
	#url(r'^account/', include('account.urls')),
	#用戶建立url，屬於accounts app下，namespace 指定命名空間

	url(r'^contact/$', views.contact, name='contact'),
	url(r'^privacypolicy/$',views.privacypolicy, name='privacypolicy'),



]


if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL,
						   document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL,
						   document_root=settings.MEDIA_ROOT)
 """
