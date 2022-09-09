from django.urls import path
from .views import NewPageView, NewDetailView, IsDoctor


urlpatterns = [
    path('', IsDoctor.as_view(), name='isdoctor'),
    path('', NewPageView.as_view(), name='news'),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail')
]
