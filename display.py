DISPLAY_WIDTH = 64
DEBUG_CONST = True

class display:
    description = ""
    mini_map = ""
    options = ""
    last_input = ""

    def __init__(self):
        print("snooping as usual I see you")
    

    def clear_screen(self, debug = False):
        """Clears screen if debug mode isnt on

        debug: Whether debug mode is enabled, if true, console isnt cleared
        """
        if not debug:
            print("\033c", end='')


    def draw(self, debug = DEBUG_CONST, turnCount = -1):
        """Refreshes the screen, redrawing all elements.

        debug: Whether debug mode is enabled, if true, console isnt cleared
        turnCount: The current turn, -1 means turn count will be hiden
        """
        self.clear_screen(debug)
        self.horizontal_line(turnCount)
        print(self.description)


    def horizontal_line(self, turnCount):
        """Prints out a horizontal line across the console of sidth determined
        by constant DISPLAY_WIDTH
        
        turnCount: The current turn, -1 means turn count will be hiden
        """
        if turnCount == -1: # TOP BAR, -1 means the turn count is hidden
            print("─"*7,"═"*(DISPLAY_WIDTH - 14),"─"*7,sep="")
        else:
            turn_string = "═╡ TURN " + str(turnCount) + " ╞" + "═"*(len(str(turnCount)) % 2)
            turn_readout_indent = ((DISPLAY_WIDTH - len(turn_string)) // 2) - 7
            print("─"*7, "═"*turn_readout_indent, turn_string, "═"*turn_readout_indent, "─"*7, sep="")


test = display()
lorum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus. Donec ultrices tincidunt arcu non sodales neque. Viverra adipiscing at in tellus integer feugiat. Consequat interdum varius sit amet mattis vulputate enim nulla. Lacinia at quis risus sed vulputate. Sagittis id consectetur purus ut faucibus pulvinar elementum. A erat nam at lectus. Amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor. Enim nulla aliquet porttitor lacus luctus. Turpis in eu mi bibendum neque. Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis. Orci sagittis eu volutpat odio facilisis mauris sit amet massa. Pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat. Vitae ultricies leo integer malesuada. Cras sed felis eget velit aliquet. Tincidunt arcu non sodales neque. Facilisi morbi tempus iaculis urna id volutpat.

Nunc pulvinar sapien et ligula ullamcorper malesuada proin. Sed nisi lacus sed viverra tellus. Et leo duis ut diam quam nulla porttitor massa. Congue nisi vitae suscipit tellus mauris a. Feugiat nibh sed pulvinar proin gravida hendrerit lectus. Euismod in pellentesque massa placerat duis. Mi ipsum faucibus vitae aliquet nec ullamcorper sit amet risus. Diam donec adipiscing tristique risus nec feugiat. Egestas quis ipsum suspendisse ultrices gravida dictum fusce. A arcu cursus vitae congue mauris rhoncus aenean vel. Est placerat in egestas erat imperdiet. Lacus vel facilisis volutpat est velit egestas dui id. Cras adipiscing enim eu turpis egestas pretium aenean. Interdum velit laoreet id donec ultrices tincidunt arcu.

Quam id leo in vitae. Nisi lacus sed viverra tellus in. Sollicitudin tempor id eu nisl nunc mi ipsum. Sapien pellentesque habitant morbi tristique senectus et netus et malesuada. Pretium lectus quam id leo in. Et ligula ullamcorper malesuada proin libero nunc consequat. Purus sit amet luctus venenatis. Ornare arcu dui vivamus arcu felis bibendum ut. Viverra justo nec ultrices dui sapien eget mi proin. Est sit amet facilisis magna etiam tempor. Sagittis eu volutpat odio facilisis mauris. Neque ornare aenean euismod elementum nisi quis eleifend. Ultrices dui sapien eget mi. Egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Pulvinar elementum integer enim neque volutpat ac tincidunt. Faucibus vitae aliquet nec ullamcorper sit amet risus nullam eget. Integer quis auctor elit sed. Eget magna fermentum iaculis eu non. Pulvinar pellentesque habitant morbi tristique senectus et. Fames ac turpis egestas sed tempus urna et.

Metus dictum at tempor commodo. Nunc pulvinar sapien et ligula. Bibendum at varius vel pharetra vel turpis nunc eget. Arcu ac tortor dignissim convallis aenean et tortor at risus. In hac habitasse platea dictumst. Nunc sed augue lacus viverra vitae congue eu consequat ac. Urna et pharetra pharetra massa massa. Purus in mollis nunc sed id semper risus in hendrerit. Commodo ullamcorper a lacus vestibulum sed arcu non odio. Ullamcorper sit amet risus nullam eget. Vitae tortor condimentum lacinia quis vel eros. Dui accumsan sit amet nulla facilisi morbi tempus. Et malesuada fames ac turpis egestas integer eget aliquet. Aliquam purus sit amet luctus venenatis lectus magna fringilla. Faucibus pulvinar elementum integer enim neque volutpat. Lectus urna duis convallis convallis.

Feugiat pretium nibh ipsum consequat nisl vel. Platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras. Lorem dolor sed viverra ipsum nunc aliquet bibendum enim facilisis. Proin libero nunc consequat interdum varius sit amet. Sed vulputate odio ut enim. Vel pretium lectus quam id leo in vitae turpis. Mus mauris vitae ultricies leo integer malesuada nunc vel. Enim eu turpis egestas pretium aenean pharetra magna ac placerat. Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula. Vulputate dignissim suspendisse in est ante in nibh. Adipiscing enim eu turpis egestas pretium aenean pharetra. Enim praesent elementum facilisis leo vel fringilla est ullamcorper eget. Id porta nibh venenatis cras sed felis. Viverra adipiscing at in tellus integer. Penatibus et magnis dis parturient montes nascetur ridiculus. Sem fringilla ut morbi tincidunt augue interdum velit euismod. Diam vel quam elementum pulvinar etiam non quam. A condimentum vitae sapien pellentesque habitant. Eu scelerisque felis imperdiet proin fermentum."""
test.description = lorum
test.draw(turnCount=5000)
test.draw(turnCount=-1)
input("   ──<press enter to exit>──   ")