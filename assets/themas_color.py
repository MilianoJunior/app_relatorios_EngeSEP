#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivy.utils import get_color_from_hex


dark = {'background':get_color_from_hex('#565050'),
         'primary': get_color_from_hex('#121212'),
         'line': get_color_from_hex('#F1F1F1'),
         'linedestaque': get_color_from_hex('#03DAC6')}

light = {'background':get_color_from_hex('#ffffff'),
         'primary': get_color_from_hex('#424242'),
         'line': get_color_from_hex('#f1f1f1'),
         'linedestaque': get_color_from_hex('#03DAC6')}

cores = {'light': light, 'dark': dark}