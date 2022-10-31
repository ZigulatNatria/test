from django.urls import path, include
from .views import CreateInfoUser, LoginView, InfoUserView


urlpatterns = [
       path('api-auth/', include('rest_framework.urls')),
       path('auth/register/', CreateInfoUser.as_view()),
       path('auth/login/', LoginView.as_view()),
       path('user/<int:pk>/', InfoUserView.as_view()),
]