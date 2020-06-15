import unittest
from app.models import Blog, User, Comment
from app import db

class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Rose = User(username = 'Rose', email = 'rose@ms.com', password = 'cairo')
        self.new_blog = Blog(title='Title for the blog',description = "pineapples")
    
    def tearDown(self):
        Blog.query.delete(self)
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.description,"pineapples")
        self.assertEquals(self.new_blog.title,'Title')

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)
