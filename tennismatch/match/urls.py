from django.urls import path, include
from rest_framework import routers
from match import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = routers.DefaultRouter()
router.register(r'all-users', views.AllCustomUserView, basename='all-users')
router.register(r'all-matches', views.AllMatchView, basename='all-matches')
router.register(r'all-messages', views.AllMessageView, basename='all-messages')
# router.register(r'post-user', views.UserList, basename='post-user')
# router.register(r'current_user/', views.current_user, basename='current-user'),

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view())
]

urlpatterns += router.urls
