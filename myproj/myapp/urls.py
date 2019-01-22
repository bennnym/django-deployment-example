from django.urls import path
from myapp import views

#TEMPLATE TAGGING

app_name = 'myapp'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative_url, name='relative')
]
