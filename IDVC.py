# Imports
import datetime as dt
import pickle as pkl
import IEM as iem

 # Variable Declarations

__version__ = 'Alpha'
__author__ = "Rodrigo 'ItsPaper' Munoz"

pause = iem.pause
cls = iem.cls
UEIP = iem.UEIP
today = dt.date.today()
sel = 0

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


def NewEntry():
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
    print('0.Salir del programa.')
    sel = MenuSel()
    print('Ha seleccionado la opcion numero ' + str(sel) + '.')
# Main

Log = Startup()
Menu()
NewEntry()
