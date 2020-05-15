import bnd_rebuilder
import unittest


class consume_byte_unit_tests(unittest.TestCase):
    def setUp(self):
        self.consume_byte_instance = bnd_rebuilder.consume_byte
    def tearDown(self):
        return super().tearDown()

class is_byte(consume_byte_unit_tests):
    def runTest(self):
        assert self.consume_byte_instance([5,5,5],5, 5, 1) == 6, \
            "not a byte"

# class extract_strz_unit_tests(unittest.TestCase):
#     def setUp(self):
#         self.extract_strz_instance = bnd_rebuilder.extract_strz
#     def tearDown(self):
#         return super().tearDown()

# class extract_strz_tests(extract_strz_unit_tests):
#     def runTest(self):
#         assert self.extract_strz_instance(b'\x00',5) == b'', \
#             "properly extracted"

class appears_bnd_unit_tests(unittest.TestCase):
    def setUp(self):
        self.appears_bnd_instance = bnd_rebuilder.appears_bnd
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

class offset_to_next_multiple_unit_test(unittest.TestCase):
    def setUp(self):
        self.offset_to_next_multiple_instance = bnd_rebuilder.offset_to_next_multiple
    def tearDown(self):
        return super().tearDown()
class is_proper_offset(offset_to_next_multiple_unit_test):
    def runTest(self):
        assert self.offset_to_next_multiple_instance(32, 35) == 3, \
            "not proper offset"

if __name__ == "__main__":
    unittest.main()
