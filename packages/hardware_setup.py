# Pushbuttons are wired between the pin and Gnd
# Pico pin  Meaning
# ESP.IO16 Up
# ESP.IO17 Left
# ESP.IO34 Right
# ESP.IO32 Down
# ESP.IO36 Center

from machine import Pin, SPI, freq

import gc
import buttons
from touch import Touch

from drivers.st7789.st7789_4bit import *
SSD = ST7789

spi = SPI(2, baudrate=40000000, polarity=1)
gc.collect()  # Precaution before instantiating framebuf
pcs = Pin(5, Pin.OUT)
pdc = Pin(33, Pin.OUT)
prst = Pin(32, Pin.OUT)
ssd = SSD(spi, height=240, width=240, cs=pcs, dc=pdc, rst=prst)

from gui.core.ugui import Display, Screen
_NEXT = const(1)
_PREV = const(2)

# Define control buttons
prv = buttons.touch_0
sel = buttons.touch_1
nxt = buttons.touch_2

class TouchInput:
    def __init__(self, prv, sel, nxt):
        self._prev = Touch(prv, 0)
        self._sel = Touch(sel, 1)
        self._next = Touch(nxt, 2)

        self._prev.press_func(Screen.ctrl_move, (_PREV,))
        self._sel.release_func(Screen.sel_ctrl)
        self._next.press_func(Screen.ctrl_move, (_NEXT,))

    def precision(self, val):
        Screen.redraw_co()

    def adj_mode(self, v=None):
        Screen.redraw_co()

    def is_adjust(self):
        return False


disp = Display(ssd, input=TouchInput(prv, sel, nxt))
