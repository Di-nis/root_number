from django.urls import path

from .views import RootApiView

urlpatterns = [
        path('create', RootApiView.as_view())
    ]
