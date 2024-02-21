from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path("",views.default,name="index"),
        path("<int:num>",views.anyNumber,name="renderTax"),
        path("taxrate",views.tax,name="tax")
]
