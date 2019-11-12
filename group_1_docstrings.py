Doc Strings

""" An adventure game that takes the user’s input to decide whether they pass the semester """ 

class Game:
	""" Structure of the adventure game, including levels, storyline, and points 	“””

	def __init__(self,name):
		“””Initializing a name and the current level, 
		Args:
			name(str): the user’s name
		Raise:
			TypeError: if the input for name is not a string 
		
		raise NotImplementedError 
        """

	def levels(self, level):
		""" Makes choices depending on current level and counts down the days till final 				grades 
		Args:
			level(int): the level the user is on 
		raise NotImplementedError """
	
    def points(self, level):		
        """ Adds or removes points based on choices in the level and will reset at every 		level
		Args:
			num_points(list): number of points gained individually that keeps track 
			level(int): the level the user is on 
		    raise NotImplementedError 
            """
	
    def storyline(self, level):
		""" Gives storyline based on current level to guide player on making decisions  
		Args:
			level(int): the level the user is on
		
		raise NotImplementedError
        """

	def parse_arg(self):
		    """Parses command line arguments.    
               Args:        
    			arglist (list of str): the command line arguments as a list of strings.    
    	         Returns:        
   			 namespace: an object containing variables and values for all declared       
    				command-line arguments.    
           
		    raise NotImplementedError
            """
def status():
	"""Keeps track of points and levels
	Return:
		The current level, points, days till final
	raise NotImplementedError
    """

def solve(name):
	"""Makes an instance of class and asks for a name
	Args: 
    name (str): the players name 
    Raise:
	ValueError: if the name of the player is not a string 
	raise NotImplementedError
    """

def grade():
	"""Determines your end grade with results from the solve method

        Return:
        grade(str): the letter grade based on how many points you have
 
	    raise NotImplementedError
    """
def main():
	""" Executes the program
	Returns:	
		Grade(str): the letter grade determined from the grade method 
		points(int): the amounts points at the end of the game 
	raise NotImplementedError
    """
if __name__ == ‘__main__’:
	raise NotImplementedError
