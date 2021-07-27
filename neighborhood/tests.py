from django.test import TestCase
from django.test import TestCase
from .models import Activity,Profile,Myloc,Post
from django.contrib.auth.models import User


class ActivityTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='Roney-juma')
    self.neighbor = Myloc.objects.create(id=1, name='home')
    self.activity = Activity.objects.create(id=1, name='Watching games', description='Watching the derby game',image='https://cloudinary url',created_at='2021,6,26',updated_at='2021,6,24', neighbor=self.neighbor,user=self.user,email='roney.juma@student.moringaschool.com')

  def test_instance(self):
    self.assertTrue(isinstance(self.activity, Activity))

  def test_create_business(self):
    self.activity.create_activity()
    business = Activity.objects.all()
    self.assertTrue(len(business) > 0)

  def test_get_activity(self, id):
    self.activity.save()
    activity = Activity.get_activity(post_id=id)
    self.assertTrue(len(activity) == 1)


class TestProfile(TestCase):
  def setUp(self):
    self.user = User(id=1, username='', password='Access')
    self.user.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.user, User))

  def test_save_user(self):
    self.user.save()

  def test_delete_user(self):
    self.user.delete()

class PostTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='Roney-juma')
    self.activity = Activity.objects.create(id=1, name='home')
    self.post = Post.objects.create(id=1, title='Watching game', post='Moringa is the best place',image='https://cloudinary url',created_at='2021,6,26',updated_at='2021,6,24',user=self.user,neighbor=self.neighbor())

  def test_instance(self):
    self.assertTrue(isinstance(self.post, Post))

  def test_display_posts(self):
    self.post.save()
    posts = Post.all_posts()
    self.assertTrue(len(posts) > 0)

  def test_save_post(self):
    self.post.save_post()
    post = Post.objects.all()
    self.assertTrue(len(post) > 0)

  def test_delete_post(self):
    self.post.delete_post()
    post = Post.search_post('random_post')
    self.assertTrue(len(post) < 1)

class NeighborhoodTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='Roney-juma')
    self.neighbor = Activity.objects.create(id=1, name='Moringa business', description='Moringa is the best place',image='https://cloudinary url',created_at='2021,6,24',updated_at='2021,6,26', neighbor=self.neighbor,user=self.user,email='roney.juma@student.moringaschool.com')

  def test_create_neighbor(self):
    self.neighbor.create_neighbor()
    neighbor = Activity.objects.all()
    self.assertTrue(len(neighbor) > 0)

  def test_get_neighbor(self, id):
    self.neighbor.save()
    neighbor = Activity.get_neighbor(neighbor_id=id)
    self.assertTrue(len(neighbor) == 1)