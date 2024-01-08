import unittest
from main import hello_world

class TestHelloWorldFunction(unittest.TestCase):

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "hello world")

if __name__ == '__main__':
    unittest.main()
