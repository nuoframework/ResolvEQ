import time
import colorama
from colorama import Fore, Style, init, Back
import math
import os

def inicio():
    print('╦═╗┌─┐┌─┐┌─┐┬ ┬  ┬╔═╗╔═╗  ') 
    print('╠╦╝├┤ └─┐│ ││ └┐┌┘║╣ ║═╬╗ ') 
    print('╩╚═└─┘└─┘└─┘┴─┘└┘ ╚═╝╚═╝╚ ') 
 

inicio()

print('Bienvenido a ResolvEQ. Desarrollado por nuoframework')

time.sleep(2)

menu = input('Eliga una opcion\n\n['+Fore.RED+'1'+Fore.RESET+']Ecuacion de segundo grado\n\n>>> ')

if menu == '1':
    a = float(input('Inserta "a": '))
    b = float(input('Inserta "b": '))
    c = float(input('Inserta "c": '))
    time.sleep(2)
    print('\nSe van a procesar las variables, esto puede tardar un poco, espere')
    time.sleep(4)
    os.system("clear")
    z = -b 
    e = b * b -4 * a * c
    d = 2 * a
    
    if e > 0:
        pass
    elif e < 0:       # En este if aseguramos que no salga un error por consola
        print('La ecuacion no tiene solucion debido a que no se puede hacer la raiz de un numero negativo')
        SystemExit
    
    if d == 0:
        print('No se puede dividir un numero entre 0')
        SystemExit
    else:
        pass
    
    raiz = math.sqrt(e)
    positive = z + raiz
    positive2 = positive / d
    negative = z - raiz
    negative2 = negative / d
    
    print('Solucion 1 = {}'.format(int(positive2)))
    print('Solucion 2 = {}'.format(int(negative2)))

    time.sleep(1200)
    SystemExit



    
