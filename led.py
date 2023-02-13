import gpiod
import time

chip = gpiod.Chip("gpiochip0")
line = chip.get_line(4)
line.request(consumer="led.py", type=gpiod.LINE_REQ_DIR_OUT)
while True:
    line.set_value(1)
    time.sleep(1)
    line.set_value(0)
    time.sleep(1)
