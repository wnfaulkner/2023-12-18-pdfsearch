# FRONTEND URLS

from django.conf.urls import path 
from main_app import views 
 
urlpatterns = [ 
  # path('accounts/signup/', views.signup, name='signup'),
  path('user-data/', views.home, name='user_data'),
  path('pdfs/', views.pdfs_index, name='pdfs_index'),
]