from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^add_airline$', views.add_airline),
    url(r'^add_airport$', views.add_airport),
    url(r'^add_country$', views.add_country),
    url(r'^add_location_to_country$', views.add_location_to_country),
]