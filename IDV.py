# File Data

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
__date__ = "16/09/18"

# Module Imports
import IEM as iem
import time
import pickle as pkl


# Variable Declarations
today = time.strftime("%c")
reports = []

# Class definitions


class Report:
    """This class will be the sales report format"""
    cc = 38815

    def __init__(self, real_ns, budget_ns, adtr, adtp, atr, atp, date):
        # Class properties
        self.real_ns = real_ns  # Real Net Sales
        self.budget_ns = budget_ns  # Budget Net Sales
        self.adtr = adtr  # Real Average daily transactions
        self.adtp = adtp  # Budget Average daily transactions
        self.atr = atr  # Real per check
        self.atp = atp  # Budget per check
        self.date = date  # Date of the report

    def review(self):
        iem.cls()
        ns_dif = self.real_ns - self.budget_ns
        ns_dif2 = (self.real_ns / self.budget_ns) * 100
        adt_dif = self.adtr - self.adtp
        adt_dif2 = (self.adtr / self.adtp) * 100
        at_dif = self.atr - self.atp
        at_dif2 = (self.atr / self.atp) * 100
        print("Report: {}".format(self.date))
        print("Net Sales: {} vs LY: {} Variation: {} or {}%.".format(self.real_ns, self.budget_ns, ns_dif, ns_dif2))
        print("ADT: {} vs LY: {} Variation: {} or {}%.".format(self.atr, self.adtp, adt_dif, adt_dif2))
        print("Per Check: {} vs LY: {} Variation: {} or {}%.".format(self.atr, self.atp, at_dif, at_dif2))
        iem.pause()


# Function Definitions


def report_log():
    try:
        reports = pkl.load(open("DataLog.data", "rb"))
    except FileNotFoundError:
        reports = []
        pkl.dump(reports, open("DataLog.data", "wb"))
    finally:
        return reports


def save(report_list):
    pkl.dump(report_list, open("DataLog.data", "wb"))
    print("Succesfully saved to DataLog.data!")


def report_entry():
    date = iem.DP()
    net_salesr = iem.UEIP("Net Sales: ", 0)
    net_salesb = iem.UEIP("Budget Net Sales: ", 0)
    adtr= iem.UEIP("ADT: ", 0)
    adtb = iem.UEIP("Budget ADT: ", 0)
    atr = iem.UEIP("Per Check: ", 0)
    atb = iem.UEIP("Budget Per Check: ", 0)
    datestr = iem.PD(date)
    entry = Report(net_salesr,net_salesb,adtr,adtb,atr,atb,date)
    entry.review()
    reports.append(entry)
    save(reports)
    return reports


# Main Code







