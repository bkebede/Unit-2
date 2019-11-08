display.scroll("Good Afternoon")

# SparkFun Electronics
# Experiment 0.1
# Display an image

from microbit import *
while True:
    display.show(Image.PACMAN) #PACMAN image shows


# SparkFun Electronics
# Experiment 0.2
# Display a custom image

from microbit import *
while True:
    star = Image("11111:99599:00000:09590:90009") #Changes shape of image
    display.show(star)

# SparkFun Electronics
# Experiment 1.0
# Blinking an LED

from microbit import *

while True:
    pin0.write_digital(1)
    sleep(1000)
    pin0.write_digital(0)
    sleep(1000)

# SparkFun Electronics
# Experiment 2.0
# Reading a Potentiometer

from microbit import *

while True:
    potVal = pin2.read_analog()
    pin0.write_analog(potVal)
    sleep(25)
