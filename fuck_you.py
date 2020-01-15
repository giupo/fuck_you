#!/usr/bin/env python

import argparse
import time

from datetime import datetime
from pymouse import PyMouse


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



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Click and wait...')
    parser.add_argument('X', metavar='X', type=int, help='screen X coordinate where to click')
    parser.add_argument('Y', metavar='Y', type=int, help='screen Y coordinate where to click')
    parser.add_argument('--sleep', default=10, dest='sleep', help='seconds to wait (default 10 seconds)')

    args = parser.parse_args()

    fuckyou = FuckYou()
    fuckyou.click_wait(args.X, args.Y, float(args.sleep))
