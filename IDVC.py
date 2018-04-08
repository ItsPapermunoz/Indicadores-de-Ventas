# Imports
import datetime as dt
import pickle as pkl
import IEM as iem

 # Variable Declarations

__version__ = 'Alpha'
__author__ = "Rodrigo 'ItsPaper' Munoz"

pause = iem.pause
cls = iem.cls
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
