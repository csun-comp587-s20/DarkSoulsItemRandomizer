import bnd_rebuilder
import unittest

# Comsume byte unit tests

class consume_byte_unit_tests(unittest.TestCase):
    def setUp(self):
        self.consume_byte_instance = bnd_rebuilder.consume_byte
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
        
# Extract STRZ unit tests

class extract_strz_unit_test(unittest.TestCase):
    def setUp(self):
        self.extract_strz_instance = bnd_rebuilder.extract_strz
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
    
class extract_strz_string(extract_strz_unit_test):
    def runTest(self):
        content = b'hello\x00' # need thex \x00 otherwise inf loop
        assert self.extract_strz_instance(content, 0) == 'hello', \
            "Expected: b'hello'"

# Appears bnd unit tests

class appears_bnd_unit_tests(unittest.TestCase):
    def setUp(self):
        self.appears_bnd_instance = bnd_rebuilder.appears_bnd
        return super().setUp()
    def tearDown(self):
        return super().tearDown()

class is_bnd(appears_bnd_unit_tests):
    def runTest(self):
        assert self.appears_bnd_instance("BND3") == True, \
            "This is not an instance of bnd"

class is_byte_garbage(appears_bnd_unit_tests):
    def runTest(self):
        assert self.appears_bnd_instance(b"MEMES") == False, \
            "This is an instance of bnd"

class is_normal_array(appears_bnd_unit_tests):
    def runTest(self):
        assert self.appears_bnd_instance([70, 38, 39, 40, 21]) == False, \
            "This is an instance of bnd"
            
# Offset next multiple unit tests

class offset_to_next_multiple_unit_tests(unittest.TestCase):
    def setUp(self):
        self.offset_to_next_multiple_instance = bnd_rebuilder.offset_to_next_multiple
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
    
class next_mult_is_zero(offset_to_next_multiple_unit_tests):
    def runTest(self):
        assert self.offset_to_next_multiple_instance(15, 0) == 0, \
            "Expected: 0"
            
class next_mult(offset_to_next_multiple_unit_tests):
    def runTest(self):
        assert self.offset_to_next_multiple_instance(15, 30) == 15, \
            "Expected: 15"
            
class next_mult_equals_offset(offset_to_next_multiple_unit_tests):
    def runTest(self):
        assert self.offset_to_next_multiple_instance(15, 15) == 0, \
            "Expected: 15"

if __name__ == "__main__":
    unittest.main()
