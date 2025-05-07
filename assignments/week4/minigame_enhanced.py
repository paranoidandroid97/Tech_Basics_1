import time

# --- Utility Functions ---

# Pause durations
def s_p():
    time.sleep(2)

def m_p():
    time.sleep(5)

def l_p():
    time.sleep(9)

# Typing effect
def typing(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def tunnel_outcome(choice):
    if choice == "1":
        typing("\nYou step into the left tunnel. It's damp and smells of moss.")
        s_p()
        typing("Suddenly the loud sound of moving stone plates penetrate your ears...")
        typing("The floor beneath you gives away!")
        s_p()
        typing("You fall into a pit of spikes and get impaled...")
        return "death"
    elif choice == "2":
        typing("\nYou venture into the right tunnel. It's dark but manageable because of your torch.")
        typing("\nYou use it to burn down the cobwebs...")
        s_p()
        typing("\nSuddenly you hear multiple screeching sounds...")
        s_p()
        typing("\nThe screeching comes from many spiders coming from the holes out of the walls... crawling towards you!")
        s_p()
        typing("\nYou run right through the many cobwebs, just hoping to flee from the spiders")
        s_p()
        typing("\nYour foot trips over a stone and you fall... just to realise you have escaped the spiders!")
        s_p()
        typing("\nLooking up you see a room, the room you were looking for.")
        typing("\nYou have found the idol!")
        s_p()
        return "success"
    else:
        typing("Confused, you stand still until a bat flies into your face.")
        typing("You stumble and hit your head. Unfortunate way to go.")
        return "death"



# --- Main Adventure Function ---

def main():
    try:
        number = int(input("Hello Adventurer! When you're ready to begin just type in a 1: "))
    except ValueError:
        print("You must type in a number to begin your adventure :)")
        return

    if number != 1:
        print("You must type in a 1 to begin your adventure :)")
        time.sleep(2)
        print("Start again...")
        return

    # Start of the game
    print("""
 _____                    _
|_   _|__ _ __ ___  _ __ | | ___
  | |/ _ \\ '_ ` _ \\| '_ \\| |/ _ \\
  | |  __/ | | | | | |_) | |  __/
  |_|\\___|_|_|_| |_| .__/|_|\\___|
   / \\   __| |_   _|_|_ _ __ | |_ _   _ _ __ ___
  / _ \\ / _` \\ \\ / / _ \\ '_ \\| __| | | | '__/ _ \\
 / ___ \\ (_| |\\ V /  __/ | | | |_| |_| | | |  __/
/_/   \\_\\__,_| \\_/ \\___|_| |_|\\__|\\__,_|_|  \\___|
""")



    s_p()
    typing("\"Welcome to the Minigame!\"")
    typing("\n\"This is not gonna be some cliche adventure. It'll be unique for sure!\"")
    typing("\n\"So let me think of something...\"")
    m_p()
    typing("\n\"Wait a second my god!\"")
    s_p()
    typing("\n\"You're probably one of these TikTok kiddies. I can tell from your attention span.\"")
    m_p()
    typing("\n\"Wait! I almost got it...\"")
    m_p()
    typing("\n\"Oh haha, yeah I know a great, non cliche start to this adventure!\"")
    s_p()
    typing("\n\"Here we go!\"\n")

    s_p()
    print("""
You awaken in a dark forest. The trees whisper in the wind.
Two paths lie before you...
""")
    m_p()
    print("""
        ||      ||
        ||      ||
     ___||______||_____
    /    1     2      /
   /                 /
  /                 /
 /                 /
/_________________/
""")
    s_p()

    choice = input("Do you take path 1 (left) or path 2 (right)? Type 1 or 2: ")

    if choice == "1":
        print("\nYou walk down the left path and hear the howling of wolves...")
    elif choice == "2":
        print("\nYou follow the right path and see the glow of a mysterious light...")
    else:
        print("You must choose 1 or 2 to proceed on your adventure!")
        return

    print("\n")
    time.sleep(5)
    typing("\"Yeah... okay. I have to admit this story isn't very original.\"")
    time.sleep(3)
    typing("\"I'll just do some Indiana Jones type shit... at least that's fun\"")

    m_p()
    print("\nYou are an adventurer and fight your way through a forest. Eventually, after days of searching, you find something.\nAn entrance to a cave. The dark, long tunnel just begs to be discovered.\nWhat will you do?")
    m_p()
    choice = input("Do you dare to enter the cave (1) or will you just turn around and leave (2)? ")

    if choice == "1":
        s_p()
        print("\nYou take the first step towards the cave entrance and light a torch to see what's in front of you. Your curiosity has won and you disappear into the darkness")
        m_p()
        print(r"""
               _______
            .-'       '-.
          .'             '.
         /   _________     \
        /   /         \\    \
       |   |           |     |
       |   |           |     |
       |   |           |     |
        \  \\_________/    /
         \             _.-'
          '._       _.-'
             '-._.-'

      (•_•)
     <)   )╯
     /   \\
     """)
    elif choice == "2":
        s_p()
        print("\nYou turn around and leave like you haven't spent the last few days searching for this. That's just kind of embarrassing.")
        s_p()
        print(r"""
        \_____/
            ( >_< )
           =\(   )>
              \ |
               |\\
              / \\==>
              """)
        exit()

    m_p()
    print("A few dozens of meters into the cave you find some ancient signs on the walls! Exactly what you were looking for.")
    m_p()
    print(r"""             ______
             |  o o |              ______
            /    -  (\            |  o o |
           / /)   (\ \\          /    -  (\
    ______| | | /) \\ \\        / /)   (\ \\
   |  o o | | || \ || | |______| | | /) \\ \\
  /    -  (\\ \\ (/ | | |  o o | | || \ || | |______
 / /)   (\ \\\ \)   (/ /    -  (\\ \\ (/ | | |  o o |
| | | /) \\ \\)  -    / /)   (\ \\\ \)   (/ /    -  (\
| | || \ || | |_o_o__| | | /) \\ \\)  -    / /)   (\ \\
 \\ \\ (/ | | |  o o | | || \ || | |_o_o__| | | /) \\ \\
  \\ \)   (/ /    -  (\\ \\ (/ | | |  o o | | || \ || | |
   \)  -    / /)   (\ \\\ \)   (/ /    -  (\\ \\ (/ | | |
    |_o_o__| | | /) \\ \\)  -    / /)   (\ \\\ \)   (/ /
    |  o o | | || \ || | |_o_o__| | | /) \\ \\)  -    /
   /    -  (\\ \\ (/ | | |  o o | | || \ || | |_o_o__|
  / /)   (\ \\\ \)   (/ /    -  (\\ \\ (/ | | |  o o |
 | | | /) \\ \\)  -    / /)   (\ \\\ \)   (/ /    -  (\
 | | || \ || | |_o_o__| | | /) \\ \\)  -    / /)   (\ \\
  \\ \\ (/ | | |  o o | | || \ || | |_o_o__| | | /) \\ \\
   \\ \)   (/ /    -  (\\ \\ (/ | | |  o o | | || \ || | |
    \)  -    / /)   (\ \\\ \)   (/ /    -  (\\ \\ (/ | | |
     |_o_o__| | | /) \\ \\)  -    / /)   (\ \\\ \)   (/ /
            | | || \ || | |_o_o__| | | /) \\ \\)  -    /
             \\ \\ (/ | | |      | | || \ || | |_o_o__|
              \\ \)   (/ /        \\ \\ (/ | | |
               \)  -    /          \\ \)   (/ /
                |_o_o__|            \)  -    /
                                     |_o_o__|
                                     """)
    m_p()
    print("\nAfter some riddling, the signs turn out to be a map of the cave leading to the hidden temple!")
    m_p()
    print("\nA few minutes later, you're faced with a mysterious hallway")
    m_p()
    print(r"""
 _____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|???????|'|,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%%%%%%%%%%%%%\____________;|
""")
    m_p()
    print("But now you have to decide in which direction you want to head.\nTo the left it seems like there is light shimmering from around the corner.\nTo the right there is another dark tunnel and a whole lot of cobwebs, with no spiders in them (hopefully)...")

    l_p()
    choice = input("So which tunnel do you want to head in? Left (1) or right (2)? ")

    outcome = tunnel_outcome(choice)

    if outcome == "death":
        typing("Your adventure ends here... better luck next time!")
        return

    m_p()
    print(r""" @#@@%@@@#@#@@+
                                       @@@@  *        @  @@@@
                                    @@ *.  .:=*@@@%@%*#*+.  #@@@
                                  ==     .-*%* .       :#@@*.   @*
                                -@ -:=.@@@@%+              #@*   %@#
                               -# .:+@@@@#@=@#*:           -%@@@:  @@
                              =@ .-@@        -@*@@%#=%@@@=+*+.=@@@. =
                              @ .=@           @%@*@@@@@=#-       @@+ @
                             @ .-  +@%:==++%%*@@ ##@@@@@@@@@@@@   @@  @
                            :-:#@@.    .:      %@@@@      : -=@@@@ @@ @
                            @ =%=   :     :-...  @   .   :  %  . --%@  @
                            @ @+  .=  @@@.   =+%=  @ =*+@ .@ @@     @@ @
                            @ @%+@ @:    *@@  @@@ @@+ @@@*+@@   @ @ .@ @
                           + @=  @:   +@@@  + @ @ @ @    @  @@@  #@@+@ @
                           @ * @@% :   @@#@#% # @ @ @-%*@@@@@@    @# @ +@  @
                        @@ @ %+  @@  +@ @ * %@@*  @%@@     :       @ @+ @@+%
                       .*-  :-     %@@@@=@-  @ @  @ @@ .     @@@@@%*@++ . -%
                        *:@ - .+@@@@%:   :  @-.@  @-:@@+#@@-  @@*@@%@== @ @-
                        *@# -+@@        @  @@ @@  +@#*@ @@@.@     ..*@*.=-=%
                        *@*:=#     +@@@@=.*.*@  @@     @@:@@@@@     @@@= @@
                            =*   @@@-    @              @#@+@@@@@    .@% @
                          @ +@*-=*   +-# @%@@@ *@@ @#@@   @==  .@=@ @=@@
                          + +:  .--::.     + @@@*@ @@@@@@** @@%    :.-@@
                           -==+  =:.@ *+-@@@#@ %@#.  .:@@@@   @:++  .-%@
                           :%-#  -:@ +%+@      += %@ *@    @@  %**  *#@+
                            %:- .@@@=-  @      - @@ @     @  @% *@..*@@
                           +*++@   @. -@@   @@@@@@      @#@@@ @@ %= @@
                           * *+@   @. +  #@.@@@@@@@@@@@@@   @ =@ @  @+
                           * .=@*  @* @ @   @      =    @ @ @*-@  -@@ #
                           +  .=@*  -*:.  @      @ @ .:.     +@  :@% =@
                           * * :=@*    =%::.==       .+###@@+*  @@* *-#
                           - @# .=@@         .%@@@@@@. +-      @@. @  @
                          = -@= = . %@      @   --+=         @%-.= @@ @
                          % %% :  @ @       :@@@@@@@@@:       :@ . :@ *
                          # @  = @: @@@@@@                :@@@*  :  *@#
                          %*+ --  :=-*-*@@@@@@@@@@@@@@@@@@@*#@@@-   *@:
                           @. --: :--   %@@@@@  -=--:%@@@@+=  .@*::  @
                           @ .-+-* #=  @@      -@@@@+     @@   @  :  *@
                          #@ .-+:@     +                    + . = -  +@
                           @ -++ @.@@@#@@@@@@@@@@@@@@@@@@@@@@@.@@-*. =@
                           @=..+@. =: #@@@@@@@%       :@@@  :@ @%=--*@
                            @+-% ..@@ @@      @@@@@     #@@=%@= @-:#@
                             @% --#@:#@@      #   %      @@:  @:+#@#
                              @ ++= +#%  +- @@@@@@@@@ *   @#  @@ @
                               -+@ :%@   @ @@-     -@@@   +@@  @@
                               #%   @@   @% @ @@@@@@ @ @@  =@   @#
                               @@   @@  @# @@ @@%@%@@ @  @ @@#  @@
                               @@  *@@  %%@  @   @   @ @ - =@@  #@
                               @*: -:  @@ @ @@ @ @ @ @. @%#     +@
                                .@@:  @+#@   @  # @  @  @ @  #@@@
                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@""")
    m_p()

    print("\nYou grab it from a little pedestal and feel the weight in your hand.")
    print("The golden Idol shimmers and it feels rewarding!")
    print("Congratulations, brave adventurer. Your journey ends in glory!")
    m_p()

    print(r"""
__   __                                _
\ \ / /__  _   _  __      _____  _ __ | |
 \ V / _ \| | | | \ \ /\ / / _ \| '_ \| |
  | | (_) | |_| |  \ V  V / (_) | | | |_|
  |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)
""")

# --- Run the game ---
if __name__ == "__main__":
    main()

