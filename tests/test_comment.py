import unittest
from app.models import Blog, User, Comment
from app import db

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(title = "title", description = "comment")
        self.new_comment = Comment(description = "pineapples", blog=self.new_blog)
    
    def tearDown(self):
        Blog.query.delete()
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.description,"pineapples")
        self.assertEquals(self.new_comment.blog,self.new_blog, 'comment')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
