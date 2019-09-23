from django.shortcuts import render
from django.view.genereic import ListView,DetailView
from django.views.genric.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Rating

class RatingListView(ListView):
	model = Rating
	template_name = 'home.html'

class RatingDetailView(DetailView):
	model = Rating
	template_name = 'detailreview.html'

class AddRatingView(CreateView):
	model = Rating
	template_name = 'addrating.html'
	fields = ['movie_name','release_year','director','rating']

class UpdateRatingView(UpdateView):
	model = Rating
	template_name = 'update.html'
	fields = ['movie_name','release_year','director','rating']

class DeleteRatingView(DeleteView):
	model = Rating
	template_name = 'delete.html'
	success_url = reverse_lazy('home')

