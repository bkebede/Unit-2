# Unit 2


### Getting Started with Micropython
My first experience with the microbit was started with the initial assignment as I had never heard of microbit prior to this. 
Initially, I saw some of the features that could be used such as displaying certain images and printing text. What was more interesting was the use of hardware such as the breadboard, resistors, etc in collaboration with the microbit. 

With the code below and hardware equipped, I was able to have LED blinking in one second intervals. 
```
while True:
    pin0.write_digital(1)
    sleep(1000)
    pin0.write_digital(0)
    sleep(1000)
```

The code below used hardware such as jumper wires, a breadboard, restistors, etc and was challenging to get working as I struggled with getting the wires and the pins placed properly. What I ended up with was the display of the LED but it wasn't blinking as it was in the prior project. This one had a knob though which could be twisted to either brighten or dim the light. 
```
while True:
    potVal = pin2.read_analog()
    pin0.write_analog(potVal)
    sleep(25)
    ```

### IoT Adventure

```
input.onButtonPressed(Button.B, () => {
    let dice = Math.randomRange(0, 5) + 1
    basic.showNumber(dice)

```
The code above was the IoT idea that I chose to modify. The code basically creates an event when the B button is pressed where a random number between 1 and 6 is selected and then shown on the microbit. 

```
Numbers = [1,2,3,4,5,6] # List of options which can be rolled

display.show('Roll dice') # Insert message prompt
while True:
  if accelerometer.was_gesture('shake'):# If user shakes, creates event
      msg = "You rolled a.. "+str(random.choice(Numbers)) # Create message telling user what was rolled
      display.scroll(msg) # Show the message  
```

The code above is what I modified the original idea into. Firstly, I changed the manner in which the number was obtained by using a list instead of the range function. I added a message prompt to the user to "Roll dice" so the user is aware there is some program in effect. Instead of pressing one of the buttons to get a number, I used a gesture in which if the microbit is shaken, an event is created. That event is rolling of the dice, where a number is returned. I added a message that tells the user they rolled whatever number pops up and I coded it to scroll that message, so the user doesn't miss it. 

### Questions regarding Unit 1...



### [Projects](https://github.com/bkebede/Unit-2)
[Getting Started with Micropython](https://github.com/bkebede/Unit-2/blob/master/Micropython.py)
[IoT Adventure](https://github.com/bkebede/Unit-2/blob/master/Dice%20Modify.py)
