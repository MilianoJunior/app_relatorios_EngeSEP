#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from controllers.excpetions.RootException import InterfaceException

def font_choice(name_font):
    try:
        const = -3
        if name_font == None:
            name_font = 'Roboto'
            fonts = {'H1': [f'{name_font}Light', 96 + const, False, -1.5],
             'H2': [f'{name_font}Light', 60 + const, False, -0.5],
             'H3': [name_font, 48 + const, False, 0],
             'H4': [name_font, 34 + const, False, 0.25],
             'H5': [name_font, 24 + const, False, 0],
             'H6': [f'{name_font}Medium', 20 + const, False, 0.15],
             'Subtitle1': [name_font, 16 + const, False, 0.15],
             'Subtitle2': [f'{name_font}Medium', 14 + const, False, 0.1],
             'Body1': [name_font, 16 + const, False, 0.5],
             'Body2': [name_font, 14 + const, False, 0.25],
             'Button': [f'{name_font}Medium', 14 + const, True, 1.25],
             'Caption': [name_font, 12 + const, False, 0.4],
             'Overline': [name_font, 10 + const, True, 1.5],
             'Icon': ['Icons', 24 + const, False, 0]}
        else:
            name_font = os.path.join(os.environ['FONTS'],name_font,name_font+'-')
            fonts = {'H1': [f'{name_font}Light', 96 + const, False, -1.5],
                     'H2': [f'{name_font}Light', 60 + const, False, -0.5],
                     'H3': [f'{name_font}Regular', 48 + const, False, 0],
                     'H4': [f'{name_font}Regular', 34 + const, False, 0.25],
                     'H5': [f'{name_font}Regular', 24 + const, False, 0],
                     'H6': [f'{name_font}Medium', 20 + const, False, 0.15],
                     'Subtitle1': [f'{name_font}Regular', 16 + const, False, 0.15],
                     'Subtitle2': [f'{name_font}Medium', 14 + const, False, 0.1],
                     'Body1': [f'{name_font}Regular', 16 + const, False, 0.5],
                     'Body2': [f'{name_font}Regular', 14 + const, False, 0.25],
                     'Button': [f'{name_font}Medium', 14 + const, True, 1.25],
                     'Caption': [f'{name_font}Regular', 12 + const, False, 0.4],
                     'Overline': [f'{name_font}Regular', 10 + const, True, 1.5],
                     'Icon': ['Icons', 24 + const, False, 0]}
        return fonts
    except Exception as e:
        raise InterfaceException(e)()
