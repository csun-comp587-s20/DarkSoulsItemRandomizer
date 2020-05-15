import bnd_rebuilder
import unittest

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

class offset_to_next_multiple(unittest.TestCase):
    def setUp(self):
        self.offset_instance = bnd_rebuilder.offset_to_next_multiple
    def tearDown(self):
        return super().tearDown()
class is_proper_offset(offset_instance):
    def runTest(self):
        assert self.offset_instance(32, 35) == 3, \
            "not a proper offset"

if __name__ == "__main__":
    unittest.main()
