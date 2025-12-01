from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),

    path('predict/', views.predict_view, name="predict"),
    path('history/', views.history_view, name="history"),

    path('admin-verify/', views.admin_verify, name="admin_verify"),
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
]
