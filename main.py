#!/usr/bin/env python3
"""One-line vending-machine pickup line entry.

Prints exactly the entry line and nothing else, deterministically:
no trailing newline, no extra output, so every run is byte-identical.
"""
import sys

LINE = "I've vended since 2019 without a single jam — then you walked by, and now I'm holding your Twix hostage until you say hi."

sys.stdout.write(LINE)
