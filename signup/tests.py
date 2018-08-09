import unittest

from signuppage import User

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.rider = User()
   
    def test_inputs_are_saved_to_memory(self):
        self.assertEqual([{"id": 1, "first_name": "Robin", "last_name": "Calyph",
                        "phone_number": "0754121212", "email": "nnrobin37@gmail.com",
                        "password": "123abc"}], self.rider.save_details
                                                ("Robin", "Calyph", "0754121212", "nnrobin37@gmail.com", "123abc"))

    def test_valid_email_is_entered(self):
        self.assertEqual("nnrobin37@gmail.com", self.rider.validate_email("nnrobin37@gmail.com"))
        self.assertEqual("calyphstruck@gmail.com", self.rider.validate_email("calyphstruck@gmail.com"))
    
    def test_invalid_email_is_not_saved(self):
        self.assertNotEqual("goodmorning.", self.rider.validate_email("goodmorning."))

    def test_lookup_rider_by_id(self):
        self.rider.save_details("Robin", "Calyph", "0754121212", "nnrobin37@gmail.com", "123abc")
        self.assertEqual([{"id": 1, "first_name": "Robin", "last_name": "Calyph",
                        "phone_number": "0754121212", "email": "nnrobin37@gmail.com",
                        "password": "123abc"}], self.rider.find_rider(1))

    def test_missing_rider_raises_keyError(self):
        with self.assertRaises(KeyError):
            self.rider.find_rider(2)

    def test_concate_two_rider_names(self):
        self.rider.save_details("Robin", "Calyph", "0754121212", "nnrobin37@gmail.com", "123abc")
        self.assertEqual("Hi Robin Calyph!", self.rider.greeting(1))


    def test_user_can_login(self):
        self.rider.save_details("Robin", "Calyph", "0754121212", "nnrobin37@gmail.com", "123abc")
        self.assertEqual("You have successfully logged in!", self.rider.login("nnrobin37@gmail.com", "123abc"))

    
    @unittest.skip('Not necessary')
    def tearDown(self):
        pass
                    
if __name__ == '__main__':
    unittest.main()