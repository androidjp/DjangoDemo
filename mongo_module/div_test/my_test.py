from django.test import TestCase


# Create your tests here.

class MyTestCase(TestCase):
    # before
    def setUp(self):
        print('====setUp=====')

    def test_add(self):
        a = 1
        b = 1
        self.assertEqual(2, a+b)
        print('finish test')

    def tearDown(self):
        print('====tearDown=====')
