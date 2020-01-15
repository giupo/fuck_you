#!/usr/bin/env python

import argparse
import time

from datetime import datetime
from pymouse import PyMouse, PyMouseEvent


class FuckYou(object):
    def __init__(self):
        self.mouse = PyMouse()

    def click(self, x, y):
        """this function generates a click where you want to."""
        self.mouse.click(x, y)

    def move(self, x, y):
        """this function moves the pointer where you want to"""
        self.mouse.move(x, y)

    def click_wait(self, x, y, sleep_time):
        """this clicks where you tell him and holds for `sleep_time` seconds"""
        while(True):
            print('[%s] Clicking (%s,%s)' % (datetime.now().isoformat(), x, y))
            self.move(x, y)
            self.click(x, y)
            time.sleep(sleep_time)


class MousePositionAtClick(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.x = None
        self.y = None

    def position(self):
        return (self.x, self.y)

    def click(self, x, y, button, press):
        if button == 1 and press:
            self.x = x
            self.y = y
            self.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Click and wait...')
    parser.add_argument(
        'sleep', metavar='sleep',
        default=10, help='seconds to wait (default 10 seconds)')

    args = parser.parse_args()

    fuckyou = FuckYou()

    print("click where you want to bust this asshole in flames...")
    get_position = MousePositionAtClick()
    get_position.run()

    
    x, y = get_position.position()
    fuckyou.click_wait(x, y, float(args.sleep))
