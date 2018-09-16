# File Data

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
__date__ = "16/09/18"

# Module Imports
import IEM as iem
import pickle as pkl
import os


# Variable Declarations
pause = iem.pause()
clear = iem.cls()
confirm = iem.confirm()

# Class definitions


class Report:
    """This class will be the sales report format"""
    cc = 38815

    def __init__(self, real_ns, Budget_ns, adtr, adtp, atr, atp):
        # Class properties
        self.real_ns = real_ns  # Real Net Sales
        self.Budget_ns = Budget_ns  # Budget Net Sales
        self.adtr = adtr  # Real Average daily transactions
        self.adtp = adtp  # Budget Average daily transactions
        self.atr = atr  # Real per check
        self.atp = atp  # Budget per check


# Function Definitions






