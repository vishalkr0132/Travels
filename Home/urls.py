from Home import views
from django.conf import settings
from django.urls import include, path

from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('packages', views.packages, name='packages'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('place/<pid>', views.about_place, name='about_place'),
    path('register', views.register_user, name="User_register"),
    path('bookingdestination/<pid>', views.bookingdestination, name='bookingdestination'),
    path('user_profile',views.user_profile, name='user_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
