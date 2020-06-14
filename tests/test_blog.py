import unittest
from app.models import Blog, User, Comment
from app import db

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.user_Rose = User(username = 'Rose', email = 'rose@ms.com', password = 'cairo')
        self.new_blog = Blog(title='Title for the blog',description = "pineapples")
    
    def tearDown(self):
        Blog.session.delete(self)
        User.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.description,"pineapples")
        self.assertEquals(self.new_blog.title,'Title for the blog')

    def test_save_blog(self):
        self.new_comment.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blogs_by_id(self):
        self.new_blog.save_comment()
        got_blogs = Blog.get_blogs(12345)
        self.assertTrue(len(got_blogs) == 1)