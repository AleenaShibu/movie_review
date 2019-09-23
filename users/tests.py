from django.test import TestCase

class UserPagesTest(TestCase):
	def test_signup_page(self):
		response = self.client.get('/users/signup/')
		self.assertTemplateUsed(response, 'signup.html')
