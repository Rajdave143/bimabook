
from django.urls import path
from .views import index, login_request
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_request, name='login'),
    # path('dashboard/', dashboard, name='dashboard')

]