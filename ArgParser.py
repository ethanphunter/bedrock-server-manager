"""
File: ArgParser.py
Author: Ethan Hunter
Description: The argument parser for bedrockServerManager
"""

import argparse
from argparse import ArgumentParser

class ArgParser(object):
    """docstring for ArgParser."""

    def __init__(self, version):
        super(ArgParser, self).__init__()
        self.version = version
        self.parser = ArgumentParser(description = "Manage Minecraft Servers")
        self.parser.add_argument('action', choices = ['start', 'stop'])
        self.parser.add_argument('server', type = str)
        self.parser.add_argument('--testing', type = bool, default = False)
        self.parser.add_argument('--version', action = 'version', version='%(prog)s ' + self.version)
