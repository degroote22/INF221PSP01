import unittest
from result import result
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_main(self):
        self.assertEqual(result("./testCases/main.txt"), "1 2 4 5 3")

if __name__ == '__main__':
    unittest.main()