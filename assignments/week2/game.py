import time
number = int(input("Hello Adventurer! When you're ready to begin just type in a 1"))
if number == 1:
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

    time.sleep(1)
    print("\"Welcome to the Minigame!\"")
    time.sleep(1)
    print("\n\"This is not gonna be some cliche adventure. It'll be unique for sure!\"")
    time.sleep(3)
    print("\n\"So let me think of something...\"")
    time.sleep(8)
    print("\n\"Wait a second my god!\"")
    time.sleep(3)
    print("\n\"You're probably one of these TikTok kiddies. I can tell from you're attention span.\"")
    time.sleep(4)
    print("\n\"Wait! I almost got it...\"")
    time.sleep(6)
    print("\n\"Oh haha, yeah I know a great, non cliche start to this adventure!\"")
    time.sleep(2)
    print("\n\"Here we go!\"")
    print("\n")

    # Now the first scene starts
    time.sleep(3)
    print("""
You awaken in a dark forest. The trees whisper in the wind.
Two paths lie before you...
""")
    time.sleep(5)
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
    time.sleep(1)

    choice = input("Do you take path 1 (left) or path 2 (right)? Type 1 or 2: ")

    if choice == "1":
        print("\nYou walk down the left path and hear the howling of wolves...")
        # that's choice number 1
    elif choice == "2":
        print("\nYou follow the right path and see the glow of a mysterious light...")
        # this is number 2
    else:
        print("You must choose 1 or 2 to proceed on your adventure!")
    print("\n")
    time.sleep(5)
    print("\"Yeah... okay. I have to admit this story isn't very original.\"")
    time.sleep(3)
    print("\"I'll just do some Indiana Jones type shit...at least that's fun\"")

    time.sleep(3)
    print("\nYou are an adventurer and fight your way trough a forest. Eventually after days of searching you find something. An entrance to a cave. The dark, long tunnel just asks to be discovered.\nWhat will you do?")

    time.sleep(5)
    choice = input("Do you dare to enter the cave (1) or will you just turn around and leave (2)?")

    if choice == "1":
        time.sleep(3)
        print("\nYou take the first step towards the cave entrance and light a torch to see what's in front of you. Your curiosity has won and you disappear into the darkness")
        time.sleep(6)
        print("""               _______
            .-'       '-.
          .'             '.
         /   _________     \\
        /   /         \\     \\
       |   |           |     |
       |   |           |     |
       |   |           |     |
        \\  \\_________/    /
         \\             _.-'
          '._       _.-'
             '-._.-'

      (•_•)
     <)   )╯
     /   \\
""")

    elif choice == "2":
        time.sleep(3)
        print("\nYou turn around and leave like you haven't spent the last few days searching for this. That's just kind of embarrassing.")
        time.sleep(3)
        print(r"""
            \_____/
            ( >_< )
           =\(   )>
              \ |
               |\\
              / \\==>
""")
        exit()

    time.sleep(7)
    print("A few dozens of meters into the cave you find some ancient signs on the walls! Exactly what you were looking for.")
    time.sleep(4)
    print(r"""
              ______
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
    time.sleep(6)
    print("\nAfter some riddling, the signs turn out to be a map of the cave leading to the hidden temple!")
    time.sleep(6)
    print("\nA few minutes after you're faced with a mysterious hallway")
    time.sleep(4)
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
    time.sleep(6)
    print("But now you have to decide in which direction you want to head.\nTo the left it seems like there is light shimmering from around the corner.\nTo the right there is another dark tunnel and a whole lot of cobwebs, with no spiders in them (hopefully)...")

    time.sleep(10)
    choice = input("So which tunnel do you want to head in? To the left, where the light is shimmering (1) or to the right where the cobwebs are obstructing your way (2)?")

    if choice == "1":
        print("Full with courage you head into the left tunnel!")
        time.sleep(4)
        print("\nAs the light seems to come closer, you step onto a brick plate...")
        time.sleep(4)
        print("\nA cold breeze blows into your face and you hear a sound of stone scratching...")
        time.sleep(4)
        print("\nThe ground underneath you begins to move and a gap forms under your feet!")
        time.sleep(4)
        print("\nYou fall down the hole and... get impaled by many up facing spears!")

        exit()

    elif choice == "2":
        print("Full of courage you head into the right tunnel!")
        time.sleep(4)
        print("\nYou use the torch to burn down the cobwebs...")
        time.sleep(4)
        print("\nSuddenly you hear multiple screeching sounds...")
        time.sleep(4)
        print("\nThe screeching comes from many spiders coming from the holes out of the walls... crawling towards you!")
        time.sleep(4)
        print("\nYou run right through the many cobwebs, just hoping to flee from the spiders")
        time.sleep(4)
        print("\nYour foot trips over a stone and you fall... just to realise you have escaped the spiders!")
        time.sleep(4)
        print("\nLooking up you see a room, the room you were looking for.")
        time.sleep(4)
        print("\nThe golden Idol on a table placed in the middle of the room")
        time.sleep(4)
        print("""



                                           @#@@%@@@#@#@@+
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
                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@



""")

        time.sleep(7)
        print(r"""
__   __                                _
\ \ / /__  _   _  __      _____  _ __ | |
 \ V / _ \| | | | \ \ /\ / / _ \| '_ \| |
  | | (_) | |_| |  \ V  V / (_) | | | |_|
  |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)
""")


else:
    print("You must type in a 1 to begin your adventure :)")
    time.sleep(2)
    print("Start again but this time try to read")

