import random
import gpiod
import time

chip0 = gpiod.Chip("gpiochip0")
chip1 = gpiod.Chip("gpiochip1")
white_line = chip0.get_line(4)
red_line = chip1.get_line(81)
yellow_line = chip1.get_line(82)
green_line = chip1.get_line(83)
white_line.request(consumer="guess.py", type=gpiod.LINE_REQ_DIR_OUT)
red_line.request(consumer="guess.py", type=gpiod.LINE_REQ_DIR_OUT)
yellow_line.request(consumer="guess.py", type=gpiod.LINE_REQ_DIR_OUT)
green_line.request(consumer="guess.py", type=gpiod.LINE_REQ_DIR_OUT)

print("Readying the LEDs!")

def leds_off():
    # set all of the lights off
    white_line.set_value(0)
    red_line.set_value(0)
    yellow_line.set_value(0)
    green_line.set_value(0)

def leds_on():
    # set all of the lights on
    white_line.set_value(1)
    red_line.set_value(1)
    yellow_line.set_value(1)
    green_line.set_value(1)

def blink_line(line):
    line.set_value(1)
    time.sleep(.3)
    line.set_value(0)
    time.sleep(.3)
    line.set_value(1)
    time.sleep(.3)
    line.set_value(0)
    time.sleep(.3)
    line.set_value(1)
    time.sleep(.3)
    line.set_value(0)


leds_off()
time.sleep(0.25)
leds_on()
time.sleep(.5)
leds_off()
print("Ready to play the guessing game!")


print("I'm thinking of a number between 0 and 100...")
x = random.randint(0, 100)
guess = -1
while guess != x:
    guess = input("Guess: ")
    if guess.isdigit():
        guess = int(guess)
    if isinstance(guess, int) == False:
        print("Please only enter integer guesses.")
        exit(0)
    if guess < x:
        print("Guess higher!")
        blink_line(red_line)
    if guess > x:
        print("Guess lower!")
        blink_line(yellow_line)
    if guess == x:
        print("Wow you won!")
        blink_line(green_line)
        green_line.set_value(1)
        break
    print("I'm still thinking of a number between 0 and 100...")
print(f"How did you know I was thinking of {x}?")
