#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pingo

board = pingo.detect.MyBoard()

led_pin = board.pins[13]
led_pin.mode = pingo.OUT

button_pin = board.pins[7]
button_pin.mode = pingo.IN


while True:
    if button_pin.state == pingo.HIGH:
        led_pin.hi()
    else:
        led_pin.lo()
