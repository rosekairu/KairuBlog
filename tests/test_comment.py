import unittest
from app.models import Blog, User, Comment
from app import db

class TestBlog(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(description = "comment")
        self.new_comment = Comment(description = "pineapples", blog=self.new_blog)
    
    def tearDown(self):
        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()      

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.description,"pineapples")
        self.assertEquals(self.new_comment.blog,self.new_blog, 'comment')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)