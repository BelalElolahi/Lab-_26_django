from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

class ThingsTests(SimpleTestCase):
    def test_home_status_code_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_template_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")


    def test_home_status_code_about_us(self):
        url = reverse('about-us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_template_about_us(self):
        url = reverse('about-us')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about_us.html")    
        