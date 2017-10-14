from django.test import TestCase
from cms.forms import BookForm
from cms.models import Book

class BookFormTest(TestCase):
    def test_valid(self):
        """正常な入力を行えばエラーにならない"""
        params = dict(name='title', publisher="publisher", page=114514)
        book = Book()
        form = BookForm(params, instance=book)
        self.assertTrue(form.is_valid())

    def test_either1(self):
        """何も入力しなければエラー"""
        params = dict()
        book = Book()
        form = BookForm(params, instance=book)
        self.assertFalse(form.is_valid())