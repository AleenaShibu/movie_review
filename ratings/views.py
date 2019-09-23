from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Ratings
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class RatingsListView(ListView):
	model = Ratings
	template_name = 'home.html'
	

class RatingsDetailView(DetailView):
	model = Ratings
	template_name = 'detailreview.html'

class AddRatingView(CreateView):
	model = Ratings
	template_name = 'addrating.html'
	fields = ['movie_name','release_year','director','review','rating']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
						

class UpdateRatingView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Ratings
	template_name = 'update.html'
	fields = ['movie_name','release_year','director','rating','review']

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class DeleteRatingView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Ratings
	template_name = 'delete.html'
	success_url = reverse_lazy('home')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user



