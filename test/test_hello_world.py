import unittest
from app.hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def test_greet(self):
        greeter = HelloWorld()
        self.assertEqual(greeter.hello_world(), "hello world")


if __name__ == "__main__":
    unittest.main()
