import shop_lineup_param
import unittest
import struct

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

class extract_shift_jisz_unit_tests(unittest.TestCase):
    def setUp(self):
        self.extract_shift_jisz_instance = shop_lineup_param.extract_shift_jisz
        return super().setUp()
    def tearDown(self):
        return super().tearDown

# class extract_shift_jisz_at_offset_test(extract_shift_jisz_unit_tests):
#     def runTest(self):
#         content = [b'\x00','thing']
#         assert '' == self.extract_shift_jisz_instance(content, 0)

# class extract_shift_jisz_later_offset(extract_shift_jisz_unit_tests):
#     def runTest(self):
#         content = [ 'b' ,'test',b'\x00']
#         b'test'.decode('shift-jis')
#         assert 'test' == self.extract_shift_jisz_instance(content,0)

class shop_lineup_unit_tests(unittest.TestCase):
    def setUp(self):
        self.shop_lineup_instance = shop_lineup_param.ShopLineup
        return super().setUp
    def tearDown(self):
        return super().tearDown

class shop_lineup_to_string_tests(shop_lineup_unit_tests):
    def runTest(self):
        test = self.shop_lineup_instance(0,0,0,0,0,0,0,0,0,"something")
        #thing = test.a
        assert str == type(test.as_string())
        assert "Id: %d (%d %d %d %d %d %d %d %d): %s" % (0, 0, 0, 0, 0, 0, 0, 0, 0, "something") == test.as_string()

class shop_lineup_to_binary_tests(shop_lineup_unit_tests):
    def runTest(self):
        test = self.shop_lineup_instance(0,0,0,0,0,0,0,0,0,"something")
        #thing = test.a
        arg = [0, 0, 0, 0, 0, 0, 0, 0]        
        testId,testData,testDescription =test.to_binary()
        assert testId == 0
        assert testDescription == "something"
        assert testData == struct.pack("@iiiiihBb", *arg) + b"\x00" * 8

class shop_lineup_param_unit_tests(unittest.TestCase):
    def setUp(self):
        self.shop_lineup_param_instance = shop_lineup_param.ShopLineupParam
        return super().setUp
    def tearDown(self):
        return super().tearDown()

class shop_lineup_param_as_string_test(shop_lineup_param_unit_tests):
    def runTest(self):
        test = self.shop_lineup_param_instance()
        assert '' == test.as_string()


if __name__ == "__main__":
    unittest.main()