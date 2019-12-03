"""An adventure game that takes the user’s input to decide whether they pass
 the semester """ 
 
import time 

class Game:
    """Structure of the adventure game, including levels, storyline,
     and points """
    
	def __init__(self,name):
		""" Initializing a name and the current level, 
		Args:
			name(str): the user’s name
		Raise:
			TypeError: if the input for name is not a string 
		"""
		raise NotImplementedError

	def levels(self, level, plot):
     """ Makes choices depending on current level and counts down the days till 
            final grades
		Args:
			level(int): the month the user is on
            plot(int): what week the user is on 
		"""
       self.level = level
       if self.level == 1:
           currentpoints = 0
           if plot == 1:
               weeks = 15
               #store how many points that choice made 
               return (self.storyline(), weeks)
           if plot == 2:
               weeks = 14
               return (self.storyline(), weeks)
           if plot == 3:
               weeks = 13
               return (self.storyline(), weeks)
           if plot == 4:
               weeks = 12
               return (self.storyline(), weeks)
       elif self.level == 2:
           if plot == 1:
               weeks = 11
               return (self.storyline(), weeks)
           if plot == 2:
               weeks = 10
               return (self.storyline(), weeks)
           if plot == 3:
               weeks = 9
               return (self.storyline(), weeks)
           if plot == 4:
               weeks = 8
               return (self.storyline(), weeks)
       elif self.level == 3:
           if plot == 1:
               weeks = 7
               return (self.storyline(), weeks)
           if plot == 2:
               weeks = 6
               return (self.storyline(), weeks)
           if plot == 3:
               weeks = 5
               return (self.storyline(), weeks)
           if plot == 4:
               weeks = 4
               return (self.storyline(), weeks)
       elif self.level == 4:
           if plot == 1:
               weeks = 3
               return (self.storyline(), weeks)
           if plot == 2:
               weeks = 2
               return (self.storyline(), weeks)
           if plot == 3:
               weeks = 1
               return (self.storyline(), weeks)
           if plot == 4:
               weeks = 0
               return (self.storyline(), weeks)

    def points(self):		
        """ Adds or removes points based on choices in the level and will 
            reset at every level
		Args:
			num_points(list): number of points gained individually that keeps track 
			level(int): the level the user is on 
		"""     
    
        current_points = [100]
    
        smallpos = ['choice1', 'choice2', 'choice3']
        mediumpos = ['choice1', 'choice2', 'choice3']
        largepos = ['choice1', 'choice2', 'choice3']
        smallneg = ['choice1', 'choice2', 'choice3']
        mediumneg = ['choice1', 'choice2', 'choice3']
        largeneg = ['choice1', 'choice2', 'choice3']
        
        for item in smallpos:
            self.current_points += 5
        
        for item in mediumpos:
            self.current_points += 10
                
        for item in largepos:
            self.current_points += 15
                
        for item in smallneg:
            self.current_points -= 5
        
        for item in mediumneg:
            self.current_points -= 10
                
        for item in largeneg:
            self.current_points -= 15
    

    def storyline(self):
        """Gives storyline to guide player on making decisions """
        
        #Possible user responses 
        answer_A = ["A", "a"]
        answer_B = ["B", "b"]
        answer_C = ["C", "c"]
        answer_D = ["D", "d"]
        yes = ["Y", "y", "yes"]
        no = ["N", "n", "no"]
        ad =("""\nYou have commited academic dishonesty by selecting an 
             invalid choice\n""")
        

        #Level = 1 plot = 1
        print("""You have just started the semester and you're a first-year and 
                you’re out of state\n 
                A: Read the syllabus B: Go to freshmen events 
                C: Buy snacks and eat out  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(1,1) 
           
        time.sleep(1)
        # plot = 2
        print("""You’ve gotten used to classes and now you’re interested in 
              clubs activities outside of classe\n 
                A: Go to first look fair B: Find a job 
                C: Drop Class  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice in answer_C:
            print("You've withdrawn from the class")
            exit()
        elif choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(1,2)
        
        time.sleep(1)
        #plot = 3
        print("""The semester has gotten heated balance your campus life is a 
              lot harder than you thought\n 
                A: Create a study plan B: Start going to office hours  
                C: Go Party  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(1,3)
        
        time.sleep(1)
        # plot = 4
        print("""First exam week what do you do\n 
                A: Last minute studying B: Follow your study plan
                C: Dream your test away  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(1,4)
        
        time.sleep(1)
        #Level = 2 plot = 1
        print("""You have completed your first exam at college you realized you 
              did poorly\n 
                A: Ride the curve B: Complain in the class group chat 
                C: Go to office hours  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(2,1)
        
        time.sleep(1)
        #Level = 2 plot = 2
        print("""You've settled in and its parents weekend\n 
                A: Go to club meet or event B: Get work done in advance  
                C: Tell your parents about your grades  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(2,2)
        
        time.sleep(1)
        #Level = 2 plot = 3
        print("""Midterms are coming\n 
                A: Go to homecoming football game B: go to the library to study 
                C: Go to office hours  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(2,3)
        
        time.sleep(1)
        #Level = 2 plot = 4
        print("""Midterms have arrived and it’s on Monday, you’re sick cuz you 
              drank too much over the weekend what do you do\n 
                A: Plan a Halloween party
                B: Go to the health center to get a note 
                C: Don't show up to class  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(2,4)
        
        time.sleep(1)
        print("""The stress has gotten to you\n 
                A: Skip Classes B: Go to the counseling center  
                C: Go to the library to pet puppies  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(3,1)
        
        time.sleep(1)
        print("""You realize you’re failing and you have talked to your 
              professor, your chances of passing are slim make your choice \n 
                A: Study extra hard  B: Drop the class with a W
                C: Go binge drink at the bar  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice in answer_B:
            print("You've withdrawn from the class")
            exit()
        elif choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(3,2)
        
        time.sleep(1)
        print("""It’s Thanksgiving when you go home are you going to study?\n 
                Yes or No """)
        choice = input(">>> ") #Input your choice.
        if choice in no:
            print("The midterm was the Monday after you've failed your class")
            exit()
        elif choice not in yes or no:
            print (ad)
            self.storyline()
        self.levels(3,3)
        
        time.sleep(1)
        print("""Last midterm\n 
                A: Panic B: Study your heart out 
                C: Go party  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(3,4)
        

        
        time.sleep(1)
        print("""Preparing for finals week\n 
                A: Go to the basketball game B: Make a finals study plan 
                C: Go party  D: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(4,1)
        
        time.sleep(1)
        print("""IT'S FINALS WEEK\n 
                A: Sleep through finals B: Take finals 
                C: [Status f(x)] """)
        choice = input(">>> ") #Input your choice.
        if choice in answer_A:
            print("You've failed your class")
            exit()
        elif choice not in answer_A or answer_B or answer_C or answer_D:
            print (ad)
            self.storyline()
        self.levels(4,2)      
        

    def parse_arg(self):
        """Parses command line arguments.    
        Args:        
            arglist (list of str): the command line arguments as a list of strings.    
        Returns:        
            namespace: an object containing variables and values for all declared       
                command-line arguments.    
        """   

            raise NotImplementedError


def status():
    """ Keeps track of points and levels
	Return:
		The current level, points, days till final
	"""
    game = Game()
    remaining = len(game.levels) - game.levels.level
    stat_lower = stat.lower()
    current = game.levels.level
    pts = game.points
  
    if stat == 'check status':
 	    print("Current Level: {}".format(current))
        print("Points: {}".format(pts))
        print("Remaining level: {}".format(remaining))


def solve(name):
	"""Makes an instance of class and asks for a name
	Args: 
        name (str): the players name 
    Raise:
	    ValueError: if the name of the player is not a string 
	"""
	raise NotImplementedError

def grade():
    """Determines your end grade with results from the solve method
    
    Return:
        grade(str): the letter grade based on how many points you have
    """
   
   results = solve(name)
   if results >= 90 :
       grade = 'A'
       return grade
   elif results >= 80:
       grade = 'B'
       return grade
   elif results >= 70 :
       grade = 'C'
       return grade
   elif results >= 60 :
       grade = 'D'
       return grade
   elif results < 60 :
       grade = 'F'
       return grade

def main():
	""" Executes the program
	Returns:	
		Grade(str): the letter grade determined from the grade method 
		points(int): the amounts points at the end of the game 
	"""
	raise NotImplementedError

if __name__ == ‘__main__’:
	raise NotImplementedError
	

