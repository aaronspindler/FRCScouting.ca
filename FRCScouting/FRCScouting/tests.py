from django.test import TestCase
from django.urls import reverse

class AccountPagesLoadTest(TestCase):
    def test_login(self):
        print("Testing Login Page")
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Accounts/login.html')

    def test_signup(self):
        print("Testing Signup Page")
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Accounts/signup.html')

class ContactPageLoadTest(TestCase):
    def test_contact(self):
        print("Testing Contact Page")
        url = reverse('contactus')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Contact/contact.html')

class BlogPagesLoadTest(TestCase):
    def test_blog(self):
        print("Testing Blog Page")
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'Blog/blogs.html')

class ScoutingPagesLoadTest(TestCase):
    def test_dashboard(self):
        print("Testing Dashboard Page")
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

class TheBlueAlliancePagesLoadTest(TestCase):
    def test_teaminfo(self):
        print("Testing Team Info Page")
        url = reverse('tba_teaminfo')
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

    def test_eventinfo(self):
        print("Testing Event Info Page")
        url = reverse('tba_eventinfo')
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

class ContentPagesLoadTest(TestCase):
    def test_home(self):
        print("Testing Home Page")
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/home.html')

    def test_about(self):
        print("Testing About Page")
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/about.html')

    def test_gamemanuals(self):
        print("Testing Game Manuals Page")
        url = reverse('gamemanuals')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/gamemanuals.html')

    def test_licenses(self):
        print("Testing Licenses Page")
        url = reverse('licenses')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/licenses.html')

    def test_matchscouting(self):
        print("Testing Match Scouting Page")
        url = reverse('matchscouting')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/matchscouting.html')

    def test_pitscouting(self):
        print("Testing Pit Scouting Page")
        url = reverse('pitscouting')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/pitscouting.html')

    def test_privacypolicy(self):
        print("Testing Privacy Policy Page")
        url = reverse('privacy')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/privacypolicy.html')

    def test_why_ads(self):
        print("Testing Why-Ads Page")
        url = reverse('why-ads')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/why-ads.html')

    def test_terms(self):
        print("Testing Terms Page")
        url = reverse('terms')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'ContentPages/terms.html')
