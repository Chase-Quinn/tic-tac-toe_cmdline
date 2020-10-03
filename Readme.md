###Starting AI Development: A Beginner's Perspective

##First Thoughts
I have been developing in Python, but mainly for the web.  Most of my time goes into Flask applications, but I really want to expand my knowledge.

Neural Networks, AI Decisions, all of this sounds familiar but at the same time completely alien to me.  Someone who hasn't been able to look into AI development might have not even heard these terms before.  So, where did I start?  I started developing a super, SUPER, simple Tic-Tac-Toe game where you play against an AI opponent.  I will discuss everything as we go, but at the same time I won't tell you everything that was actually learned until the end.  So stay tuned!

##Getting Started
Of course, we need to set up our IDE if we haven't already, I already did so I am going to keep going.  There are already plenty of "First Setup" videos and articles online to get you started if you haven't.  Then, I am going to plan my file structure so everything stays organized.

##Prerequisites
The only thing I believe should be actually known before you start this is basic Python, logic flow, loops, conditionals, things of that nature.  Other than that, just the ability to type out the code of course!

##First Steps
First things first, I created a folder to hold the game code.  I named mine "tic-tac-toe_cmdline", that is just my logic at play here.  cmdline means command line, since this will not be using a GUI.  You can name it whatever you want to, so get creative!

##Organization is King!
Once we have our main folder, lets create our sub-folders.  This will hold different Python files, or modules, that we can import and use.  The reason for this is so our main Python file does not overflow with code.  It makes it so much more readable and mainainable.

Structure is as follows:
tic-tac-toe_cmdline/
	ai
	gamebuilder
	gamelogic

Okay, so now our folders are created.  Now we can get to coding.  This flow helps me a ton in the long run, and I hope it gives you some insight on your own style of organizing code.

##Starting to Code!
The first file I create is 'tic-tac-toe.py'.  This is where the main game loop will be located, along with any function calls to outside modules.  So in a sense, this is the game 'controller'.  You don't have to do this, but I usually put a print() inside this just so I can see it in the terminal/command prompt.

If you are reading this within the repository, see tic-tac-toe_cmdline/screenshots/screenshot1.png.

Now, lets add an array to hold the game's areas that will hold the x's and o's.

Navigate to your gamebuilder folder and create a file named 'gameboard.py'.  Now, we can create the board for our game!

Here is the code:
----------
# The array that contains the positions available in the board, in total there are 9
pos = [' ' for x in range(9)]
----------

This is my favorite way of doing this, currently there are 9 empty spaces within the pos array. 'pos' stands for position, just an fyi!

If you want, print that array to make sure everything is function and run the file within your terminal/command prompt!

If you are reading this within the repository, see tic-tac-toe_cmdline/screenshots/screenshot2.png

Now, let's build the board!  This will seem... super repetitive, and it is but we only have to do it once!

Inside gamebuilder/ lets create a board that will show up in the command line!  The code is below:

# This is the function for command line tic-tac-toe board, 
# everything is for graphics minus the positions for the letters.

def createBoard(pos):
    showBoard = '''
         {pos[0]} | {pos[1]} | {pos[2]}
         ---------
         {pos[3]} | {pos[4]} | {pos[5]}
         ---------
         {pos[6]} | {pos[7]} | {pos[8]}
        '''.format(pos = pos)

    print(showBoard)

You can call this function to print the board on the prompt if you are wanting to see it in action... before we actually get everything working of course!

##Adding Some Game Logic
Okay, now let's add some logic so the user can select which they would rather be (x's or o's)!

Navigate to gamelogic/ and create a file named 'player.py'
