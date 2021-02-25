#!/usr/bin/env python3
"""
Write a Python program to get height and width of the console window.
"""

print("--- my solution ---")

print("--- w3resource solution ---")

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())
