"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from books.models import Publisher
from django.utils import unittest
from django.test.client import Client

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PubTestCase(unittest.TestCase):
    def setUp(self):
        #self.supushank = Publisher.objects.create(name="supushank", address="abc",city="calcutta", state_province="canada", website="supushank.com")
        
        self.supushank = Publisher.objects.create(name="supushank", address="abc",city="calcutta", state_province="canada", website="supushank.com")
    def test_pub_case(self):
        self.assertEqual(self.supushank.website,"supushank.com")

class BookViewsTestCase(unittest.TestCase):

    def setUp(self):
        self.supushank = Publisher.objects.create(name="supushank", address="abc",city="calcutta", state_province="canada", website="supushank.com")

    def test_duplicate_website_throws_error(self):
        c = Client()
        resp = c.post('/add_publisher/', {'name':'supushank', 'address':'j', 'city': 'j', 'state_province': 'j', 'website': 'supushank.com'})
        self.assertEqual(resp.status_code, 200)

    def test_valid_entry_is_saved(self):
        c = Client()
        resp = c.post('/add_publisher/', {'name':'supushank1', 'address':'j', 'city': 'j', 'state_province': 'j', 'website': 'supushank1.com'})
        self.assertEqual(resp.status_code, 200)

