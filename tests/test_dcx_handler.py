import dcx_handler
import unittest

# Comsume byte unit tests

class consume_byte_unit_tests(unittest.TestCase):
    def setUp(self):
        self.consume_byte_instance = dcx_handler.consume_byte
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


class appears_dcx_unit_tests(unittest.TestCase):
    def setUp(self):
        self.appears_dcx_instance = dcx_handler.appears_dcx
    def tearDown(self):
        return super().tearDown()
    
class is_dcx(appears_dcx_unit_tests):
    def runTest(self):
        assert self.appears_dcx_instance(b"DCX\x00") == True, \
            "This is not an instance of dcx"

class is_byte_garbage(appears_dcx_unit_tests):
    def runTest(self):
        assert self.appears_dcx_instance(b"MEMES") == False, \
            "This is an instance of dcx"

class is_normal_array(appears_dcx_unit_tests):
    def runTest(self):
        assert self.appears_dcx_instance([-1, 2, 5, -8, 7]) == False, \
            "This is an instance of dcx"

if __name__ == "__main__":
    unittest.main()
