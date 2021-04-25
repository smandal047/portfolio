from django.test import TestCase
from my_works_blog.models import Project, Post


# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(title="TestProject1", short_description="Test1")
        Project.objects.create(title="TestProject2", short_description="Test2")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        test_1 = Project.objects.get(title="TestProject1")
        test_2 = Project.objects.get(title="TestProject2")

        self.assertEqual(test_1.short_description, 'Test1')
        self.assertEqual(test_2.short_description, 'Test2')


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(post_title="TestPost1")
        Post.objects.create(post_title="TestPost2")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        test_1 = Post.objects.get(post_title="TestPost1")
        test_2 = Post.objects.get(post_title="TestPost2")

        self.assertEqual(test_1.body, None)
        self.assertEqual(test_2.body, None)
