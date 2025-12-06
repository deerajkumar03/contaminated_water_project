from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),

    path('forgot-password/', views.forgot_password_view, name="forgot_password"),
    path('reset-password/<str:username>/', views.reset_password_view, name="reset_password"),

    path('predict/', views.predict_view, name="predict"),
    path('history/', views.history_view, name="history"),
]
