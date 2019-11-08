from microbit import *
import random

Numbers = [1,2,3,4,5,6] # List of options which can be rolled

display.show('Roll dice') # Insert message prompt
while True:
    if accelerometer.was_gesture('shake'):# If user shakes, creates event
        msg = "You rolled a.. "+str(random.choice(Numbers)) # Create message telling user what was rolled
        display.scroll(msg) # Show the message


# Mods: Created a list, inserted message prompt, display message with number rolled after user shakes microbit



    

