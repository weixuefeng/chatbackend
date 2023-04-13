from django.test import TestCase


# Create your tests here.
class UserTest(TestCase):

    def setUp(self):
        pass

    def test_completions(self):
        data = {
            "prompt": "你好"
        }
        r = self.client.post('/api/v1/user/completions/', data)
        result = r.json()
        print(result)

    def test_chat(self):
        data = {
            "prompt": "你好"
        }
        r = self.client.post('/api/v1/user/chat/', data)
        result = r.json()
        print(result)

    def test_image(self):
        data = {
            "prompt": "home icon"
        }
        r = self.client.post('/api/v1/user/images/', data)
        result = r.json()
        print(result)
