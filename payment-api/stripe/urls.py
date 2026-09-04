from django.urls import  path

from .views import AccountView

urlpatterns = [
    path("stripe/", AccountView.as_view(), name="stripe-page")
]
