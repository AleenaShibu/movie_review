from django.db import models
#from star_ratings import get_star_ratings_rating_model_name
from django.urls import reverse
from django.contrib.auth import get_user_model


class Ratings(models.Model):
	rating = [('*','1'),
	        ('**','2'),
	        ('***','3'),
	        ('****','4'),
	         ('*****','5')]
	movie_name = models.CharField(max_length=50)
	release_year = models.CharField(max_length=4)
	director = models.CharField(max_length=30)
	review = models.TextField()
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,)
	#ratings = GenericRelation(get_star_ratings_rating_model_name()
	rating = models.CharField(max_length=5, choices=rating, default='1')
	poster = models.ImageField(upload_to='poster/', blank =True)

	def __str__(self):
		return self.movie_name[ :50]
	def get_absolute_url(self):
		return reverse('detail', args=[str(self.id)])	


