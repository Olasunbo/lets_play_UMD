import unittest 
import math
import time
import final

class TestGame(unittest.TestCase):
    def setUp(self): 
        filename = 'test.json'   
        self.g = final.Game(filename)
            
    def test_init(self):
        """ Test whether init method sets attributes correctly."""
        self.assertIsInstance(self.g, final.Game)
        self.assertIsNot(self.g.player_points, 0)
        self.assertIsNot(self.g.week, 1)
        self.assertIsNot(self.g.week, 14) 
        
    def test_stats(self):
        ts = self.g.stats(6)
        self.assertEqual(self.g.player_points, 7)
        
    def test_sanitize(self):
                
        self.assertTrue(self.g.sanitize("yes").isupper())
        self.assertEqual(self.g.sanitize('yes').upper(), "Y")
        self.assertTrue(self.g.sanitize("no").isupper())
        self.assertEqual(self.g.sanitize('no').upper(), "N")
        
class TestFunctions:
        
    def test_main(self):
        print("Start : %s" %time.ctime())
        time.sleep( 2 )
        print("End : %s" %time.ctime())
        print("Start : %s" %time.ctime())
        time.sleep( 3 )
        print("End : %s" %time.ctime())
        print("Start : %s" %time.ctime())
        time.sleep( 7 )
        print("End : %s" %time.ctime())
        print("Start : %s" %time.ctime())
        time.sleep( 1 )
        print("End : %s" %time.ctime())
        

        
if __name__ == "__main__":
    unittest.main() 