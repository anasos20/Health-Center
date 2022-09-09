from django.views.generic import ListView, DetailView

from doctors.models import Doctor

from .models import News


class NewPageView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'newsapp/news_list.html'


class NewDetailView(DetailView):
    model = News
    template_name = 'newsapp/new_detail.html'


class IsDoctor(ListView):
    model = Doctor
    context_object_name = 'doctors'

    def get_queryset(self):
        doctor_query = Doctor.objects.all()
        return doctor_query
    template_name = 'newsapp/news_list.html'
