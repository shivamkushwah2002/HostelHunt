from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from app import views
from . import views
urlpatterns = [
    path("", views.index,name='index'),
    path("home/", views.home,name='home'),
    path("login/", views.login_page,name='login'),
    path("logout/", views.logout_page,name='logout'),
    path("admin/", views.logout,name='admin'),
    path('listing/', views.listing, name='add_listing'),
    path('home/view_details/<int:id>/', views.view_details, name='view_details'),
    path('register/',views.register,name="regi"),
    path('owner/',views.owner,name="owner"),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path('update/<int:listing_id>/', views.update_listing, name='update_listing'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)