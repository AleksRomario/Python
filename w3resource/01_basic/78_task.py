#!/usr/bin/env python3
"""
Write a Python program to find the available built-in modules.
"""

print("--- my solution ---")



print("--- w3resource solution ---")

import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
# sys.builtin_module_names - кортеж строк, содержащий имена всех доступных модулей.

print(textwrap.fill(module_name, width=70))
# textwrap.fill(text, width=70, **kwargs)
# Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph.

