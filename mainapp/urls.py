from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('50/', views.fifty, name="fifty"),
    path('search/', views.search, name="search"),
    path('home', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('cities/<str:city>', views.cities, name="cities"),
    path('planner/<str:city>', views.planner, name="planner"),
    path('about', views.about, name="about"),
    path('law', views.law, name="law"),
    path('suggest', views.suggest, name="suggest"),
]
