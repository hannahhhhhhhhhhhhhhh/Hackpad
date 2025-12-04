import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules import Layer
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.Display import Display, TextEntry, DISPLAY_OLED
import adafruit_ssd1306 

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
display = Display(
    display_type=DISPLAY_OLED, 
    i2c_address=0x3C,
    i2c_bus=1, 
    flip=True,
)

kbd = Keyboard(usb_hid.devices)
keyboard.pins_col = [board.GPIO2, board.GPIO4, board.GPIO03]
keyboard.pins_row = [board.GPIO6, board.GPIO7, board.GPIO0]
switch1 = digitalio.DigitalInOut(board.D5)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(board.D6)
switch2.switch_to_input(pull=digitalio.Pull.UP)

switch3 = digitalio.DigitalInOut(board.D7)
switch3.switch_to_input(pull=digitalio.Pull.UP)

switch4 = digitalio.DigitalInOut(board.D8)
switch4.switch_to_input(pull=digitalio.Pull.UP)


keyboard.pins = {
    board.D5: KC.A,  # Switch 1 mapped to KC.A
    board.D6: KC.B,  # Switch 2 mapped to KC.B
    board.D7: KC.C,  # Switch 3 mapped to KC.C
    board.D8: KC.D,  # Switch 4 mapped to KC.D
}


layer1 = Layer([KC.LSFT, KC.LCTL, KC.LALT])


keyboard.modules.append(layer1)


if __name__ == "__main__":
    while True:
        keyboard.poll()
