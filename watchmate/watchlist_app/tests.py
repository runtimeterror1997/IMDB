from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testUser', password= 'test123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name='example1', about='example', website='https://example.com')
    
    def test_stream_platform_create(self):
        data = {
            'name': 'example',
            'about': 'i am example',
            'website': 'https://example.com'
        }
        
        response = self.client.post(reverse('stream'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_stream_platform_list(self):
        response = self.client.get(reverse('stream'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_stream_platform_detail(self):
        response = self.client.get(reverse('stream-detail', args = (self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
class WatchListTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testUser', password= 'test123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name='example1', about='example', website='https://example.com')
        
        self.watchlist = models.WatchList.objects.create(title='movie', platform=self.stream, description='example', active= True)
        
    def test_create_watchlist(self):
        data = {
            'platform': self.stream,
            'title': 'example movie',
            'description': 'i am example',
            'active': True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        
    def test_watchlist(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_stream_platform_detail(self):
        response = self.client.get(reverse('movie-detail', args = (self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
class ReviewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testUser', password= 'test123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name='example1', about='example', website='https://example.com')
        
        self.watchlist = models.WatchList.objects.create(title='movie', platform=self.stream, description='example', active= True)
        
    def test_review_create(self):
        data = {
            "rating": 3,
            "description" : 'I am description',
            "active" : True,
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    