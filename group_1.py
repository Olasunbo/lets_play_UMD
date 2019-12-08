

import unittest
import lets_play

class TestGame(unittest.TestCase):
	
    def setup(self):
        self.ex = lets_play.Game("Bob")
		


    def test_init(self):
        name = 2
 	    #test that a typeerror is raised if name is not a character
  	    self.assertRaises(TypeError, lambda: self.__init__(name))


    def test_levels(self):
        """Test to make sure that level is an int """
       
        self.assertTrue(type(self.levels()) is int)
		
        with self.assertRaises(NotImplementedError):
            GameClass().methodToRaise(NotImplementedError)

    def test_points(self):
        """Tests if points are added or removed based on choices."""
        self.assertIsNotNone(self.level)
		#test if list is updated when points are added or removed
        with self.assertRaises (NotImplementedError):
            GameClass().methodToRaise(NotImplementedError)

    def test_storyline(self):

    def test_parse_arg(self):
	    """Tests input and parsing of command line arguments. """
        self.parser = Game()
        self.assertIsNotNone(input) 
        with self.assertRaises (NotImplementedError):
            GameClass().methodToRaise(NotImplementedError)
	

class TestFunctions(unittest.TestCase):

    def test_status(self):
	
        """ Keeps track of the points and levels completed and stores that information 
		In a dictionary"""
        self.assertTrue(type(lets_play.Game.stats) is dict())

	
    def test_solve(self):
        """Creates an instance of the Game Class"""
        self.assertIsInstance(self.ex, lets_play.Game)

        self.assertTrue(type(self.ex.name, is str())
		
        with self.assertRaises(ValueError):
            self.assertFalse(type(self.ex.name) is str())

    def test_grade(self):
        """To test whether the points are in range and are given a grade letter """
        self.g = lets_play.Game()
        self.r = “will be an int”
        self.assertEqual(self.g.points(),self.r)
        self.assertTrue(self.grade(), is str)
        with self.assertRaises (NotImplementedError):
            GameClass().methodToRaise(NotImplementedError)
            
    def test():

# main test procedure 
# user starts program and should be prompted for their name 
# after completing the simulations the main function should return a grade 
# and the amount of points gained in the game