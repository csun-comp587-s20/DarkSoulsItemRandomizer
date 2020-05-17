import dcx_handler
import unittest
from dcx_handler import compress_dcx_content
from dcx_handler import uncompress_dcx_content

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


#compress/decompress unit tests
class compress_dcx_content_unit_tests(unittest.TestCase):
    def setUp(self):
        self.compress_dcx_instance = dcx_handler.compress_dcx_content
    def tearDown(self):
        return super().tearDown()

class uncompress_dcx_content_unit_tests(unittest.TestCase):
    def setUp(self):
        self.uncompress_dcx_instance = dcx_handler.uncompress_dcx_content
    def tearDown(self):
        return super().tearDown()

class uncompress_test(uncompress_dcx_content_unit_tests):
    def runTest(self):
        comp = compress_dcx_content(b'MEMES')
        assert self.uncompress_dcx_instance(comp) == b'MEMES', \
            "uncompression pass"

# class compress_test(compress_dcx_content_unit_tests):
#     def runTest(self):
#         uncomp = uncompress_dcx_content(b'MEMESMEMES')
#         assert self.compress_dcx_instance(uncomp) == b'MEMES', \
#             "compression pass"

if __name__ == "__main__":
    unittest.main()
