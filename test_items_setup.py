import items_setup
import unittest

# Item lot part unit tests

class item_lot_part_unit_tests(unittest.TestCase):
    def setUp(self):
        self.item_lot_part_instance = items_setup.ItemLotPart()
    def tearDown(self):
        return super().tearDown()
    
# class flag_error(item_lot_part_unit_tests):
#     def runTest(self):
#         assert self.


# Boss weapon list helper unit tests

class boss_weapon_list_helper_unit_tests(unittest.TestCase):
    def setUp(self):
        self.boss_weapon_list_instance = items_setup.boss_weapon_list_helper
    def tearDown(self):
        return super().tearDown()

class list_of_five(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(0, 400) == \
            [(0, 0), (0, 100), (0, 200), (0, 300), (0, 400)], \
                "The lists are not equivalent"

class list_of_one(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(0, 0) == [(0, 0)], \
            "The lists are not equivalent"

class list_of_zero(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(0, -1) == [], \
            "The lists are not equivalent"

class inverted_indices(boss_weapon_list_helper_unit_tests):
    def runTest(self):
        assert self.boss_weapon_list_instance(400, 0) == [], \
            "The lists are not equivalent"

if __name__ == "__main__":
    unittest.main()
