from django.test import TestCase
from django.urls import reverse

class AccountPagesLoadTest(TestCase):
    def test_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Accounts/login.html')

    def test_signup(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Accounts/signup.html')

class ContactPageLoadTest(TestCase):
    def test_contact(self):
        url = reverse('contactus')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Contact/contact.html')

class BlogPagesLoadTest(TestCase):
    def test_blog(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Blog/allblogs.html')

class ScoutingPagesLoadTest(TestCase):
    def test_dashboard(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

class TheBlueAlliancePagesLoadTest(TestCase):
    def test_teaminfo(self):
        url = reverse('tba_teaminfo')
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

class ContentPagesLoadTest(TestCase):
    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/home.html')

    def test_about(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/about.html')

    def test_gamemanuals(self):
        url = reverse('gamemanuals')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/gamemanuals.html')

    def test_licenses(self):
        url = reverse('licenses')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/licenses.html')

    def test_matchscouting(self):
        url = reverse('matchscouting')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/matchscouting.html')

    def test_pitscouting(self):
        url = reverse('pitscouting')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/pitscouting.html')

    def test_privacypolicy(self):
        url = reverse('privacy')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/privacypolicy.html')

    def test_why_ads(self):
        url = reverse('why-ads')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/why-ads.html')

    def test_why_ads(self):
        url = reverse('why-ads')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/why-ads.html')
