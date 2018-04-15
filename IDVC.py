# Imports
import datetime as dt
import pickle as pkl
import IEM as iem
import os

 # Variable Declarations

__file__ = 'IDVC.py'
__version__ = 'Beta'
__author__ = "Rodrigo 'ItsPaper' Munoz"

pause = iem.pause
cls = iem.cls
UEIP = iem.UEIP
today = dt.date.today()
sel = 0


# Class Declarations


class Entry:
    """Class containing the variables of an entry"""
    def __init__(self, VtaAA, Vta, VtaVar, VtaVar2, ChecksAA, Checks, ChecksVar, ChecksVar2, ATAA, AT, ATVar, ATVar2, Fecha):
        self.VtaAA = VtaAA
        self.Vta = Vta
        self.VtaVar = VtaVar
        self.VtaVar2 = VtaVar2
        self.ChecksAA = ChecksAA
        self.Checks = Checks
        self.ChecksVar = ChecksVar
        self.ChecksVar2 = ChecksVar2
        self.ATAA = ATAA
        self.AT = AT
        self.ATVar = ATVar
        self.ATVar2 = ATVar2
        self.Fecha = Fecha

    def Reporte(self):
        cls()
        print('-----Fecha de entrada: ' + str(self.Fecha) + ' -----')
        print('\n-----  Resultado Semanal ano anterior  -----\n')
        print('Venta: ' + str(self.VtaAA))
        print('Transacciones: ' + str(self.ChecksAA))
        print('Ticket Promedio: ' + str(self.ATAA) + "\n")
        pause()
        print('\n-----  Resultado Semanal actual  -----\n')
        print('Venta: ' + str(self.Vta))
        print('Transacciones: ' + str(self.Checks))
        print('Ticket Promedio: ' + str(self.AT) + "\n")
        pause()
        print('\n-----  Variacion  -----')
        print('\nVenta: ' + str(self.VtaVar) + ' ' + str(self.VtaVar2) + '%')
        print('Transacciones: ' + str(self.ChecksVar) + ' ' + str(self.ChecksVar2) + '%')
        print('Ticket Promedio: ' + str(self.ATVar) + ' ' + str(self.ATVar2) + '%')
        pause()



# Function Definitons

def Startup():
    try:
        Log = pkl.load(open('Log.data', 'rb'))
    except:
        Log = 0
        print('Iniciando proceso de primer uso...')
        pause()
        pkl.dump(Log, open('Log.data', 'wb'))
    return Log


def EntryDump(entrada):
    FileName = 'Entradas/' + str(today) + '.data'
    pkl.dump(entrada, open(FileName, 'wb'))


def NewEntry():
    Fecha = today
    VtaAA = UEIP('Ingrese la venta acumulada semanal del ano anterior: ', 0)
    Vta = UEIP('Ingrese la venta acumulada semanal: ', 0)
    ChecksAA = UEIP('Ingrese la cantidad de transacciones del ano anterior: ', 0)
    Checks = UEIP('Ingrese la cantidad de transacciones: ', 0)
    ATAA = UEIP('Ingrese el ticket promedio del ano anterior: ', 0)
    AT = UEIP('Ingrese el ticket promedio: ', 0)
    VtaVar = Vta - VtaAA
    VtaVar2 = (Vta * 100) / VtaAA
    ChecksVar = Checks - ChecksAA
    ChecksVar2 = (Checks * 100) / ChecksAA
    ATVar = AT - ATAA
    ATVar2 = (AT * 100) / ATAA
    cls()
    print('-----  Resultado Semanal ano anterior  -----\n')
    print('Venta: ' + str(VtaAA))
    print('Transacciones: ' + str(ChecksAA))
    print('Ticket Promedio: ' + str(ATAA) + "\n")
    pause()
    print('\n-----  Resultado Semanal actual  -----\n')
    print('Venta: ' + str(Vta))
    print('Transacciones: ' + str(Checks))
    print('Ticket Promedio: ' + str(AT) + "\n")
    pause()
    print('\n-----  Variacion  -----')
    print('\nVenta: ' + str(VtaVar) + ' ' + str(VtaVar2) + '%')
    print('Transacciones: ' + str(ChecksVar) + ' ' + str(ChecksVar2) + '%')
    print('Ticket Promedio: ' + str(ATVar) + ' ' + str(ATVar2) + '%')
    pause()
    entrada = Entry(VtaAA, Vta, VtaVar, VtaVar2, ChecksAA, Checks, ChecksVar, ChecksVar2, ATAA, AT, ATVar, ATVar2, Fecha)
    EntryDump(entrada)


def ReadEntries():
    x = os.listdir('Entradas')
    i = 1
    for entry in x:
        print('Entrada ' + str(i) + '. ' + str(entry))
        i += 1
    entrySel = UEIP('Seleccione el numero de entrada para leer: ', 0)
    entrySel -= 1
    sel = x[entrySel]
    entry = pkl.load(open('Entradas/' + sel, 'rb'))
    entry.Reporte()


def MenuSel():
    print("Seleccione la opcion deseada.")
    try:
        sel = int(input('Opcion Numero: '))
    except:
        print('Seleccione una opcion Valida.')
        sel = int(input('Opcion Numero: '))
    return sel


def Menu():
    cls()
    print('*****  Menu Principal  *****')
    print('1.Nueva entrada.')
    print('2.Leer Entradas')
    print('0.Salir del programa.')
    sel = MenuSel()
    print('Ha seleccionado la opcion numero ' + str(sel) + '.')
    if sel == 1:
        NewEntry()
    elif sel == 2:
        ReadEntries()
# Main

Log = Startup()
Menu()
