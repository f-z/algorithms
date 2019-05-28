#!/bin/python3
# Convert string with decimal integer to hex speak


def convert_to_hex_speak(string):
    h = hex(int(string)).split('x')[-1]
    h = h.replace('0', 'O')
    h = h.replace('1', 'I')
    allowed = set('ABCDEFIO')

    if set(h) <= allowed:
        return h.upper()

    return 'ERROR'
