import chr_init_param
import unittest

<<<<<<< HEAD
# 
=======
# Extract shift jisz unit tests

class extract_shift_jisz_unit_tests(unittest.TestCase):
    def setUp(self):
        self.shift_jisz_instance = chr_init_param.extract_shift_jisz
    def tearDown(self):
        return super().tearDown()

# Find chr by id unit tests

class find_chr_by_id_tests(unittest.TestCase):
    def setUp(self):
        self.find_chr_by_id_instance = chr_init_param.find_chr_by_id
    def tearDown(self):
        return super().tearDown()

class find_nonexistent_char():
    def runTest(self):
        assert self.find_chr_by_id_instance('B') == False, \
            "chr id's should be numbers"
>>>>>>> 5e66989e7192c1748e0eeea998f87d1410ae9666

if __name__ == "__main__":
    unittest.main()
