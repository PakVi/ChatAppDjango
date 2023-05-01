from django.urls import path

from . import views

from .views import SignUp, edit


urlpatterns = [
    path('profile/', edit, name='profile'),
    # path('signup/', views.signup, name='signup'),
    path('signup/', SignUp.as_view(), name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]