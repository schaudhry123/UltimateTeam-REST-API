from django.conf.urls import url, include
from restapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^teams/getSimulation/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', views.get_simulation)
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]