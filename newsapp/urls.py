from django.urls import path
from .views import NewPageView
urlpatterns = [
    path('', NewPageView.as_view(), name='news')
]
