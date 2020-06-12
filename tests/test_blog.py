import unittest
from app.models import Blog, User, Comment
from app import db

class TestBlog(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'Rose',password = 'cairo', email = 'rose@ms.com')
        self.new_blog = Blog(description = "pineapples", title='fruits')
    
    def tearDown(self):
        Blog.session.delete(self)
        User.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.description,"pineapples")
        self.assertEquals(self.new_blog.title,'fruits')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_blogs_by_id(self):
        self.new_blog.save_comment()
        got_blogs = Blog.get_blogs(12345)
        self.assertTrue(len(got_blogs) == 1)