from django.urls import path

from .views import RootApiView

urlpatterns = [
        path('', RootApiView.as_view())
    ]
