from django.db import models
#from star_ratings import get_star_ratings_rating_model_name
from django.urls import reverse


class Rating(models.Model):
	movie_name = models.CharField(max_length=50)
	release_year = models.CharField(max_length=4)
	director = models.CharField(max_length=30)
	review = models.TextField()
	#ratings = GenericRelation(get_star_ratings_rating_model_name()
	rating = models.CharField(options=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****'))]
	def __str__(self):
		return self.movie_name[ :50]
	def get_absolute_url(self):
		return reverse('detailreview', args=[str(self.id)])	


