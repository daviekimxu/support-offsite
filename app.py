#!/usr/bin/env python
from scripts.pulse import pulse
from scripts.rainbow import rainbow
from scripts.1d_tetris import 1d_tetris
# from scripts.weather import weather
# from scripts.twitter import twitter
import blinkt

def lights():
    effect = 1d_tetris
    effect()

if __name__ == '__main__':
    lights()
