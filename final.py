"""An adventure game that takes the user’s input to decide whether they pass
 the semester """ 
 
import time
import json
import sys 

class Game:
    """Structure of the adventure game, including levels, storyline,
     and points 
     
     Attributes:
        player_points(int): the points accumulated by the player in game
     """
    player_points = 0
    
    def __init__(self, file):
        """ Initializing a name and the current current month and week, current 
                and read in story 
		Args:
			name(str): the user’s name
		Raise:
			TypeError: if the input for file is not a string 
		"""
        with open(file,encoding="utf-8")as f:
            self.stories = json.load(f)
        
        self.month = 1 
        self.week = 14
        self.storyline()
        
    def stats(self, points):
        """ Will contain player stats in the game including the current month 
                and week the player is on and the points as well
		Args:
			points(int):amount of points from player choice 
             
		"""
        self.week -= 1
        self.player_points += points
        if self.week >= 1 and self.week <= 4:
            self.month = 1
        elif self.week >= 5 and self.week <= 8:
            self.month = 2
        elif self.week >= 9 and self.week <= 12:
            self.month = 3
        else:
            self.month = 4
    

    def storyline(self): 
        """Gives storyline to guide player on making decisions """
        for story in self.stories:
            print(story['Plot'])
            print()#prints newline
            time.sleep(1)
            choices = story['Choices']#made a refrence to the dict choices
            self.event(choices)
                    
    
    def event(self, choices):
        while True: #until made a valid choice could be a function
            for choice in choices:
                #print the choice variable (the key in choices and called the 
                # dict and key to print associated text)
                print(choice,choices[choice]["Text"])
            actual_answer = input(">>> ")
            answer =  self.sanitize(actual_answer)
            if answer not in choices:
                print ("Invalid choice please pick again")
                continue
            else:
                if "Action" in choices[answer]:
                    act = choices[answer]["Action"]
                    self.reaction(act, answer)
                else:
                    self.stats(choices[answer]["Point"])
                    break 
            
                        
    def reaction(self, action, answer):
        choices = self.stories['Choices']
        if action == "Status":
            self.status()
            time.sleep(5)
        elif action == "Exit Game":
            print(choices[answer]["Reason"])
            time.sleep(1)
            exit() 
            
                    
    def sanitize(self,answer): 
        correct = answer.upper()
        if correct == "YES":
            correct = "Y"
        elif correct == "NO":
            correct = "N" 
        return correct     
          

    def status(self):
        """ Keeps track of points and levels
        Return:
            The current current month, points, and days till final
        """
        
        remaining = self.week*7
        current = self.month
        pts = self.player_points
    
        
        print("You are currently on month: {}".format(current))
        print("You have {} points".format(pts))
        print("Remaining days till final grades are out: {}".format(remaining))



def grade(story):
    """Determines your end grade with results
    
    Args:
        story: json file with storyline in it 
    
    Return:
        grade(str): the letter grade based on how many points you have
    """
    g = Game(story)
    results = g.player_points
    if results >= 90:
        grade = 'A'
        return grade
    elif results >= 80:
        grade = 'B'
        return grade
    elif results >= 70:
        grade = 'C'
        return grade
    elif results >= 60:
        grade = 'D'
        return grade
    elif results < 60:
        grade = 'F'
        return grade

def main(name):
    """ Executes the program
    Returns:	
		Grade(str): the letter grade determined from the grade method 
		points(int): the amounts points at the end of the game 
	"""
    print("Welcome To Let's Play UMD")
    
    time.sleep(2)
    print ("This is an text based adventure game where you the user will be")
    print("presented with the option to make or break your grade\n")
    
    time.sleep(3)
    print("""Each choice is worth various amount of points that you can't see\n 
          These points will add or subtract from your grade so make wise 
          choice\n
          You have the option of viewing your status in the game by selecting 
          the status optioin avalible at every plot\n 
          It's one class, you start off with 0 points, and you have 98 DAYS TILL
          FiNALS\n """)
    
    time.sleep(7)
    print("NOW LET'S PLAY\n")  
    print("good luck %s ..... (you might need it)\n" % (name))
    
    print("Congrats you got a %s" % (grade('demo.json')))
    time.sleep(1)

    
if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    position = 1
    while (arguments >= position):
        print ("Player %i: %s" % (position, sys.argv[position]))
        position = position + 1
    main(sys.argv[1:])
	

