import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

#On board led
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False

#assign button pins
# Get keycodes from https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py
btn1_pin = board.GP15
btn2_pin = board.GP14
btn3_pin = board.GP13
btn4_pin = board.GP12

#get keyboard
keyboard = Keyboard(usb_hid.devices)

#assign button characteristics
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

#define rotary encoder
dirPin = digitalio.DigitalInOut(board.GP16)
stepPin = digitalio.DigitalInOut(board.GP17)
dirPin.direction = digitalio.Direction.INPUT
stepPin.direction = digitalio.Direction.INPUT
encSw = digitalio.DigitalInOut(board.GP18)#encoder button



#enable pull up
dirPin.pull = digitalio.Pull.UP
stepPin.pull = digitalio.Pull.UP
encSw.pull = digitalio.Pull.UP
previousValue = True#keep track of what previous value of step pin is

cc = ConsumerControl(usb_hid.devices)

led.value = True

while True:
    #encoder stuff
    if previousValue != stepPin.value:
        if stepPin.value == False:
            if dirPin.value == False:
                # print("To the right")
                # Raise volume.
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            else:
                # print("To the left")
                # Lower volume.
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        previousValue = stepPin.value
    if encSw.value == 0:
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.2)
    #button stuff
    if btn1.value:
        # print("button 1 pressed")
        keyboard.press(Keycode.ALT, Keycode.TAB)
        time.sleep(0.2)
        keyboard.release(Keycode.ALT, Keycode.TAB)
    if btn2.value:
        # print("button 2 pressed")
        keyboard.press(Keycode.WINDOWS, Keycode.TAB)
        time.sleep(0.2)
        keyboard.release(Keycode.WINDOWS, Keycode.TAB)
    if btn3.value:
        # print("button 3 pressed")
        keyboard.press(Keycode.WINDOWS, Keycode.V)
        time.sleep(0.2)
        keyboard.release(Keycode.WINDOWS, Keycode.V)
    if btn4.value:
        # print("button 4 pressed")
        keyboard.press(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)
        time.sleep(0.2)
        keyboard.release(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)
    
    # time.sleep(0.1)



