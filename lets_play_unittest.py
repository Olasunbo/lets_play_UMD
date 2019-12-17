import unittest 
import math
import final

class TestGame(unittest.TestCase):
    
    def test_init(self):
        pass
        
        
    def test_stats(self):
        pass
        
    def test_storyline(self):
        pass
        
    def test_reaction(self):
        pass
        
    def test_event(self):
        pass
    
    def test_sanitize(self):
        
        gc = final.Game
        
        self.assertTrue(gc.sanitize(self,"yes").isupper())
        self.assertEqual(gc.sanitize(self,'yes').upper(), "Y")
        self.assertTrue(gc.sanitize(self,"no").isupper())
        self.assertEqual(gc.sanitize(self,'no').upper(), "N")
        
    def test_status(self):
        pass
        
        
class TestFunctions:
        
    def test_grade(self):
        
        self.g = final.Game()
        self.r1 = 95
        self.r2 = 55
        self.assertEqual(self.g.playerpoints,self.r1)
        self.assertTrue(self.grade(story).resutlt, self.g.playerpoints)
        self.assertTrue(self.grade(story), is str)
        self.assertEqual(self.grade(story), "A")
        self.assertEqual(self.g.playerpoints,self.r2)
        self.assertTrue(self.grade(story).resutlt, self.g.playerpoints)
        self.assertTrue(self.grade(story), is str)
        self.assertEqual(self.grade(story), "F")
        
        
    def test_main(self):
        pass

if __name__ == "__main__":
    unittest.main()        

    