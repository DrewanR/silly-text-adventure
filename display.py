import os

DISPLAY_WIDTH = 80
DEBUG_CONST = False
GAME_ALIGN = 0
"""
DISPLAY_WIDTH: the width of the main play area, must be no more than 8 cells less than terminal width
BEBUG_CONST: True: Debug mode will be on, resulting in console not getting cleared alignment may br ignored
GAME_ALIGN: controls the game's alignment within the console
"""
BF = " " * 0 # BF, buffer size, used to create the margin, placed here for readability

class display:
    description = ""
    mini_map = ""
    options = ""
    last_input = ""

    next_print = ""

    def __init__(self):
        print("snooping as usual I see you")
    

    def clear_screen(self, debug = False):
        """Clears screen if debug mode isnt on

        debug: Whether debug mode is enabled, if true, console isnt cleared
        """
        if not debug:
            print("")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")


    def Draw(self, debug = DEBUG_CONST, turnCount = -1):
        """Refreshes the screen, redrawing all elements.

        debug: Whether debug mode is enabled, if true, console isnt cleared
        turnCount: The current turn, -1 means turn count will be hiden
        """
        self.clear_screen(debug)
        self.horizontal_line(turnCount)
        self.print_textbox(self.description)


    def horizontal_line(self, turnCount):
        """Prints out a horizontal line across the console of sidth determined
        by constant DISPLAY_WIDTH
        
        turnCount: The current turn, -1 means turn count will be hiden
        """
        if turnCount == -1: # TOP BAR, -1 means the turn count is hidden
            print("─"*7,"═"*(DISPLAY_WIDTH - 14),"─"*7,sep="")
        else:
            turn_string = "═╡ TURN " + str(turnCount) + " ╞" + "═"*(len(str(turnCount)) % 2)
            turn_readout_indent = ((DISPLAY_WIDTH - len(turn_string)) // 2) - 11
            print(BF, " "*5,"─"*7, "═"*turn_readout_indent, turn_string, "═"*turn_readout_indent, "─"*7, " "*5, sep="")

    
    def reset_width(self, width):
        if width > 0:
            return width - 8
        else:
            return DISPLAY_WIDTH


    def print_textbox(self, text, width = -1):
        """Prints out a text box, handling new lines etc.

        text: the text to be printed can be: an array/list (1 element = 1 line) or string
        width: the width of text allowed can be:
            *-1 <default>: infer from WIDTH constant
            *int x:          fixed width of value specified, x
            *tuple x y:      the first x lines will have width y, before using const
        *TODO
        """
        if type(text) == str:
            text = text.split("\n")
        
        text = map(lambda s : s.split(" "), text)

        for line in text:
            width_remaining = self.reset_width(width)
            print("\n  ",end="")
            for word in line:
                if len(word) + 1 <= width_remaining:
                    print(word, end=" ")
                    width_remaining -= len(word) + 1
                else:
                    width_remaining = self.reset_width(width)
                    print("\n  ", word, sep="", end=" ")
                    width_remaining -= len(word) + 1
                


test = display()
lorum = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus."""
test.description = lorum
test.Draw(turnCount=5000)
input()
test.Draw(turnCount=-1)
input("   ──<press enter to exit>──   ")
print("","1","2","3","4","5","6","7","8","9","0", sep=" "*9)
print("1234567890"*10)
test.horizontal_line(-1)