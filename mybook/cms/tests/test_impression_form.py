from django.test import TestCase
from cms.forms import ImpressionForm
from cms.models import Impression


class ImpressionFormTests(TestCase):
    def test_valid(self):
        """正常な入力を行えばエラーにならないことを検証"""
        params = dict(comment='感想')
        impression = Impression()
        form = ImpressionForm(params, instance=impression)
        self.assertTrue(form.is_valid())

    def test_either(self):
        """何も入力しなければエラーになることを検証"""
        params = dict()
        impression = Impression()
        form = ImpressionForm(params, instance=impression)
        self.assertFalse(form.is_valid())