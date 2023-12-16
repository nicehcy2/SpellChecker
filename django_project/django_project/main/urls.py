from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', spellcheck, name='spellcheck'),
    path('result/<str:input_text>/<str:result_text>/<int:error_count>/', result_page, name= 'result_page'),
]
