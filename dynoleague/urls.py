"""dynoleague URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from league import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('draftpicks', views.draft_pick_list, name='picks-list'),
    path('rosters', views.league_rosters, name='rosters'),
    path('', views.home, name='home'),
    path('leaguerules', views.league_rules, name='rules'),
    path('historyview', views.history, name='history'),
    path('updateplayers', views.update_players_view, name='updater'),
    path('team/<pk>', views.teams, name='team'),
]
