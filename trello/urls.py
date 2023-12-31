"""trello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers                 
from django.conf.urls.static import static
from django.conf import settings
from main import views 

router = routers.DefaultRouter()                   
router.register(r'current-user', views.CurrentUserView, 'current-user')
router.register(r'users', views.UsersView, 'users')
router.register(r'boards', views.BoardsView, 'boards')
router.register(r'workspaces', views.WorkspacesView, 'workspaces')
router.register(r'cards', views.CardsView, 'cards')
router.register(r'lists', views.ListsView, 'lists')
router.register(r'checklists', views.ChecklistsView, 'checklists')
router.register(r'labels', views.LabelsView, 'labels')
router.register(r'list-item', views.ListItemsView, 'list-item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('landing.urls')),
    path('<str:view>/', include(('main.urls', 'main'), namespace='main')),
    path('api/', include(router.urls)),
    path(r'logout', views.LogoutView.as_view(), name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
