from django.test import TestCase

class RatingPageTest(TestCase):
	def test_login_page(self):
		response = self.client.get('/users/signup/')
		self.assertTemplateUsed(response, 'signup.html')


		
