from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MovieList
# from django.views.generic.edit import FormView
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .filter import MovieFilter


class HomePageView(ListView):
    model = MovieList
    template_name = 'index.html'
    context_object_name = 'movie_list'
    # queryset = MovieList.objects.order_by('upload_date')[:8]
    # ordering = ['-upload_date']
    
    def get_queryset(self):
        return self.model.objects.order_by('-upload_date')

class DetailPageView(DetailView):
    model = MovieList
    template_name = 'detail.html'
    context_object_name = 'movie'


class HollywoodPageView(ListView):
    model = MovieList
    template_name = 'hollywood.html'
    context_object_name = 'movie_list'
    

    def get_queryset(self):
        return self.model.objects.order_by('-upload_date')

    

class BollywoodPageView(ListView):
    model = MovieList
    template_name = 'bollywood.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return self.model.objects.order_by('-upload_date')


class TollywoodPageView(ListView):
    model = MovieList
    template_name = 'tollywood.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return self.model.objects.order_by('-upload_date')


class WebSeriesPageView(ListView):
    model = MovieList
    template_name = 'web_series.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return self.model.objects.order_by('-upload_date')


def contact(request):
    title = 'Request a Movie'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        emailFrom = form.cleaned_data['email']
        comment = form.cleaned_data['movie_name']
        subject = 'Movie Request'
        text = 'Movie Name: %s ==> NAME: %s ==> EMAIL: %s' % (
            comment, name, emailFrom)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, text, emailFrom, emailTo, fail_silently=False)
        title = 'Thanks'
        confirm_message = "We'll upload the movie as soon as possible. Keep visiting.."
        form = None

    context = {'title': title, 'form': form,
               'confirm_message': confirm_message}
    template = 'request_movie.html'
    return render(request, template, context)

def search(request):
    movie_list = MovieList.objects.all()
    movie_filter = MovieFilter(request.GET, queryset=movie_list)
    return render(request, 'search_list.html', {'filter':movie_filter})
