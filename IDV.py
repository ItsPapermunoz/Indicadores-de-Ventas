# File Data

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
__date__ = "22/09/18"

# Module Imports
import IEM as iem
import time
import pickle as pkl


# Variable Declarations
today = time.strftime("%c")

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
    """Tries to find a previous DataLog.data File, creates a new one if FileNotFound Exception is run"""
    try:
        reports = pkl.load(open("DataLog.data", "rb"))
    except FileNotFoundError:
        reports = []
        pkl.dump(reports, open("DataLog.data", "wb"))
    finally:
        return reports


def save(report_list):
    """Dumps report list into Datalog.data"""
    pkl.dump(report_list, open("DataLog.data", "wb"))
    print("Succesfully saved to DataLog.data!")


def report_entry():
    """Creates a new report"""
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
    print("Report entry successful!")
    iem.pause()
    return reports


def report_del():
    """Deletes a report entry"""
    if len(reports) == 0:
        print("There are no reports!")
        iem.pause()
        return
    else:
        i = 1
        for report in reports:
            date = iem.PD(report.date)
            print("Report number {}. Date: {}".format(i, date))
            i += 1
        while True:
            try:
                del_prompt = iem.UEIP("Which Report number do you want to delete? ", 0)
                del_prompt -= 1
                reports.remove(reports[del_prompt])
                save(reports)
                print("Report successfully deleted!")
                iem.pause()
                return reports
            except IndexError:
                print("There is no such report...")
                iem.pause()


def report_view():
    if len(reports) == 0:
        print("There are no reports to view!")
        iem.pause()
        return
    else:
        i = 1
        for report in reports:
            date = iem.PD(report.date)
            print("Report number {}. Date: {}".format(i, date))
            i += 1
        while True:
            try:
                view_prompt = iem.UEIP("Which report do you want to Preview? ", 0)
                view_prompt -= 1
                view_prompt = reports[view_prompt]
                view_prompt.review()
                break
            except IndexError:
                print("There is no such report...")
                iem.pause()


def wipe(report_list):
    print("Are you sure you want to delete all reports?")
    if iem.confirm():
        report_list = []
        save(report_list)
        print("Data successfully wiped...")
        iem.pause()
        return report_list
    else:
        iem.pause()
        return report_list


def menu(reports):
    """This is the main Menu Loop. that runs all of the functions based on the  user option selection"""
    while True:
        iem.cls()
        print("Welcome to ItsPaper's Sales indicator.")
        print("Please Select one of the following options...")
        print("Option 1. View Reports\nOption 2. Enter a new Report\nOption 3. Delete an existing report")
        print("Option 4. Wipe all data\nOption 5. Credits\nOption 6. Exit Program!")
        menusel = iem.UEIP("\nPlease enter the number of the option... ", 0)
        if menusel == 1:
            iem.cls()
            report_view()
        elif menusel == 2:
            iem.cls()
            reports = report_entry()
        elif menusel == 3:
            iem.cls()
            reports = report_del()
        elif menusel == 4:
            iem.cls()
            reports = wipe(reports)
        elif menusel == 5:
            iem.cls()
            print("ItsPaper's Sales indicator\n Made by: {}.".format(__author__))
            print("Last Edited: {} Current Version loaded: {}".format(__date__, __version__))
            print("Contact me at: {}".format(__email__))
            iem.pause()
        elif menusel == 6:
            iem.cls()
            print("Thank you for using ItsPaper's Sales Indicator!")
            iem.pause()
            break
        else:
            print("Option not recognized, please try again!")
            iem.pause()


# Main Code

reports = report_log()
menu(reports)






