from django.db import models
from django.utils import timezone


categories = (
    ('hollywood', 'hollywood',),
    ('bollywood', 'bollywood',),
    ('tollywood', 'tollywood',),
    ('web_series', 'web_series',),
)

class MovieList(models.Model):
    cat = models.CharField(max_length=20, choices=categories,default='hollywood')
    title_main = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=18)
    year = models.IntegerField(default=2020)
    imdb_rating = models.FloatField()
    cast = models.TextField()
    director = models.CharField(max_length=254)
    movie_type = models.CharField(max_length=254)
    language = models.CharField(max_length=254, default='Hindi')
    thumbnail = models.ImageField(upload_to='')
    torrent_link_1080 = models.TextField(null = True, blank=True)
    torrent_link_720 = models.TextField(null = True, blank=True)
    direct_link_720 = models.TextField(null = True, blank=True)
    upload_date = models.DateTimeField(default=timezone.now())
    
    
    def __str__(self):
        return self.title
    
    
