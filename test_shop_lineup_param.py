import shop_lineup_param
import unittest

# Comsume byte unit tests

class consume_byte_unit_tests(unittest.TestCase):
    def setUp(self):
        self.consume_byte_instance = shop_lineup_param.consume_byte
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
    
class is_content_byte(consume_byte_unit_tests):
    def runTest(self):
        content = b'DCX\x00'
        assert self.consume_byte_instance(content, 0, b'D', 1) == 1, \
            "Expected: 1"
            
class is_content_is_not_byte(consume_byte_unit_tests):
    def runTest(self):
        content = b'DCX\x00'
        self.assertRaises(ValueError, self.consume_byte_instance, content, 0, b'D', 3)

if __name__ == "__main__":
    unittest.main()