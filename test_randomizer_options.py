import randomizer_options
import unittest

# Random option difficulty tests

class rand_opt_difficulty_unit_tests(unittest.TestCase):
    def setUp(self):
        self.rand_opt_difficulty_instance = \
            randomizer_options.RandOptDifficulty
        return super().setUp()
    def tearDown(self):
        return super().tearDown()

# can be improved with a property-based generator
class rand_opt_difficulty_garbage(rand_opt_difficulty_unit_tests):
    def runTest(self):
        # Passing 0 corresponds to being Easy difficulty
        assert self.rand_opt_difficulty_instance.as_string("1g>$)-/") == "", \
            "Expected: \"\""
    
class rand_opt_difficulty_easy(rand_opt_difficulty_unit_tests):
    def runTest(self):
        # Passing 0 corresponds to being Easy difficulty
        assert self.rand_opt_difficulty_instance.as_string(0) == "Fair", \
            "Expected: \"Fair\""
            
class rand_opt_difficulty_medium(rand_opt_difficulty_unit_tests):
    def runTest(self):
        # Passing 1 corresponds to being Medium difficulty
        assert self.rand_opt_difficulty_instance.as_string(1) == "Unfair", \
            "Expected: \"Unfair\""

class rand_opt_difficulty_hard(rand_opt_difficulty_unit_tests):
    def runTest(self):
        # Passing 2 corresponds to being Hard difficulty
        assert self.rand_opt_difficulty_instance.as_string(2) == "Very Unfair", \
            "Expected: \"Very Unfair\""

# Random option key difficulty tests

class rand_opt_key_difficulty_unit_tests(unittest.TestCase):
    def setUp(self):
        self.rand_opt_key_difficulty_instance = \
            randomizer_options.RandOptKeyDifficulty
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
    
class rand_opt_key_difficulty_garbage(rand_opt_key_difficulty_unit_tests):
    def runTest(self):
        assert self.rand_opt_key_difficulty_instance.as_string("1g>$)-/") == "", \
            "Expected: \"\""
        
class rand_opt_key_difficulty_leave_alone(rand_opt_key_difficulty_unit_tests):
    def runTest(self):
        # Passing 0 corresponds to being LEAVE_ALONE status
        assert self.rand_opt_key_difficulty_instance.as_string(0) == "Not Shuffled", \
            "Expected: \"Not Shuffled\""

class rand_opt_key_difficulty_randomize(rand_opt_key_difficulty_unit_tests):
    def runTest(self):
        # Passing 1 corresponds to being RANDOMIZE status
        assert self.rand_opt_key_difficulty_instance.as_string(1) == "Shuffled", \
            "Expected: \"Shuffled\""

class rand_opt_key_difficulty_race_mode(rand_opt_key_difficulty_unit_tests):
    def runTest(self):
        # Passing 2 corresponds to being RACE MODE status
        assert self.rand_opt_key_difficulty_instance.as_string(2) == "Race Mode", \
            "Expected: \"Race Mode\""

class rand_opt_key_difficulty_race_mode_plus(rand_opt_key_difficulty_unit_tests):
    def runTest(self):
        # Passing 3 corresponds to being RACE MODE + status
        assert self.rand_opt_key_difficulty_instance.as_string(3) == "Race Mode +", \
            "Expected: \"Race Mode +\""
            
# Random option start items difficulty tests

class rand_opt_start_items_difficulty_unit_tests(unittest.TestCase):
    def setUp(self):
        self.rand_opt_start_items_difficulty_instance = \
            randomizer_options.RandOptStartItemsDifficulty
        return super().setUp()
    def tearDown(self):
        return super().tearDown()

class rand_opt_start_items_difficulty_garbage(rand_opt_start_items_difficulty_unit_tests):
    def runTest(self):
        assert self.rand_opt_start_items_difficulty_instance.as_string("1g>$)-/") == "", \
            "Expected: \"\""
            
class rand_opt_start_items_difficulty_shield_and_one_hand(rand_opt_start_items_difficulty_unit_tests):
    def runTest(self):
        # Passing 0 corresponds to SHIELD_AND_1H status
        assert self.rand_opt_start_items_difficulty_instance.as_string(0) == "Shield & 1H Weapon", \
            "Expected: \"Shield & 1H Weapon\""

class rand_opt_start_items_difficulty_shield_and_two_hand(rand_opt_start_items_difficulty_unit_tests):
    def runTest(self):
        # Passing 1 corresponds to SHIELD_AND_2H status
        assert self.rand_opt_start_items_difficulty_instance.as_string(1) == "Shield & 1/2H Weapon", \
            "Expected: \"Shield & 1H Weapon\""

class rand_opt_start_items_difficulty_combined_pool_and_two_hand(rand_opt_start_items_difficulty_unit_tests):
    def runTest(self):
        # Passing 2 corresponds to COMBINED_POOL_AND_2H status
        assert self.rand_opt_start_items_difficulty_instance.as_string(2) == "Shield/Weapon & Weapon", \
            "Expected: \"Shield/Weapon & Weapon\""

# Random option soul items difficulty tests

class rand_opt_soul_items_difficulty_unit_tests(unittest.TestCase):
    def setUp(self):
        self.rand_opt_soul_items_difficulty_instance = \
            randomizer_options.RandOptSoulItemsDifficulty
        return super().setUp()
    def tearDown(self):
        return super().tearDown()

class rand_opt_soul_items_difficulty_garbage(rand_opt_soul_items_difficulty_unit_tests):
    def runTest(self):
        assert self.rand_opt_soul_items_difficulty_instance.as_string("1g>$)-/") == "", \
            "Expected: \"\""

class rand_opt_soul_items_difficulty_shuffle(rand_opt_soul_items_difficulty_unit_tests):
    def runTest(self):
        # Passing 0 corresponds to SHUFFLE status
        assert self.rand_opt_soul_items_difficulty_instance.as_string(0) == "Shuffled", \
            "Expected: \"Shuffled\""

class rand_opt_soul_items_difficulty_consumable(rand_opt_soul_items_difficulty_unit_tests):
    def runTest(self):
        # Passing 1 corresponds to CONSUMABLE status
        assert self.rand_opt_soul_items_difficulty_instance.as_string(1) == "Replaced", \
            "Expected: \"Replaced\""

class rand_opt_soul_items_difficulty_transpose(rand_opt_soul_items_difficulty_unit_tests):
    def runTest(self):
        # Passing 2 corresponds to TRANSPOSE status
        assert self.rand_opt_soul_items_difficulty_instance.as_string(2) == "Transposed", \
            "Expected: \"Transposed\""

# Random option game version tests

class rand_opt_game_version_unit_tests(unittest.TestCase):
    def setUp(self):
        self.rand_opt_game_version_instance = \
            randomizer_options.RandOptGameVersion
        return super().setUp()
    def tearDown(self):
        return super().tearDown()

class rand_opt_game_version_garbage(rand_opt_game_version_unit_tests):
    def runTest(self):
        assert self.rand_opt_game_version_instance.as_string("1g>$)-/") == "", \
            "Expected: \"\""

class rand_opt_game_version_ptde(rand_opt_game_version_unit_tests):
    def runTest(self):
        assert self.rand_opt_game_version_instance.as_string("DARK SOULS: Prepare To Die Edition") == \
            "DARK SOULS: Prepare To Die Edition", \
            "Expected: \"DARK SOULS: Prepare To Die Edition\""

class rand_opt_game_version_remastered(rand_opt_game_version_unit_tests):
    def runTest(self):
        assert self.rand_opt_game_version_instance.as_string("DARK SOULS: REMASTERED") == \
            "DARK SOULS: REMASTERED", \
            "Expected: \"DARK SOULS: REMASTERED\""

# Random option game version tests

class randomizer_options_unit_tests(unittest.TestCase):
    def setUp(self):
        self.randomizer_options_instance = \
            randomizer_options.RandomizerOptions
        return super().setUp()
    def tearDown(self):
        return super().tearDown()

class randomizer_options_all_off_and_first_options_except_mixup(randomizer_options_unit_tests):
    def runTest(self):
        self.randomizer_options_instance = \
            randomizer_options.RandomizerOptions(0, 0, 0, 0, 0, 0, 0, "DARK SOULS: Prepare To Die Edition", 1)
        assert self.randomizer_options_instance.as_string() == \
            "Randomizer Settings:\n" \
            "  Game Version: DARK SOULS: Prepare To Die Edition\n" \
            "  Difficulty: Fair\n" \
            "  Fashion Souls: Off\n" \
            "  Key Difficulty: Not Shuffled\n" \
            "  Senile Gwynevere: Off\n" \
            "  Senile Primordial Serpents: Off\n" \
            "  Soul Items: Shuffled\n" \
            "  Starting Items: Shield & 1H Weapon\n" \
            "  Laundromat Mixup: On\n" \
            , \
            "Expected: \n" \
            "Randomizer Settings:\n" \
            "  Game Version: DARK SOULS: Prepare To Die Edition\n" \
            "  Difficulty: Fair\n" \
            "  Fashion Souls: Off\n" \
            "  Key Difficulty: Not Shuffled\n" \
            "  Senile Gwynevere: Off\n" \
            "  Senile Primordial Serpents: Off\n" \
            "  Soul Items: Shuffled\n" \
            "  Starting Items: Shield & 1H Weapon\n" \
            "  Laundromat Mixup: On\n"

if __name__ == "__main__":
    unittest.main()