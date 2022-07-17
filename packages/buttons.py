# define buttons

from machine import Pin, Signal, TouchPad

# The only usuable physical button on the badge
BTN_BOOT = 0

boot_pin = Pin(BTN_BOOT)
boot_button = Signal(boot_pin, invert=True)

# Touch controls available as simulated buttons
touch_0 = TouchPad(Pin(27)) # P0 - BIG, Touch7
touch_1 = TouchPad(Pin(14)) # P1 - BIG, Touch6
touch_2 = TouchPad(Pin(13)) # P2 - BIG, Touch4

touches = [touch_0, touch_1, touch_2]



# The buttons on the GameOn addon
