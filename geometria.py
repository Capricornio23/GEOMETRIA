#!/usr/bin/python3

import sys
import os
import time
import os as sistema

# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue

os.system('clear')


def pedirOpcionCorrecta():
	print (""+G+"")
	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input("Elige una opcion: "))
			correcto=True
		except ValueError:
			print('Error, Elige una opcion correcta: ')

	return num

salir = False
opcion = 0

while not salir:
	print (""+R+"")
	print ("""
   __   ___   __         ___ ____   __       _
  / _  (_    /  )  /|/| (_    /    /__)  /  /_|
 (__)  /__  (__/  /   | /__  (    / (   (  (  |
	""")
	print (""+O+"Este script sirve para calcular el área de las")
	print (""+O+"figuras geométricas que se muestran en el menú")
	print ("")
	print (""+G+"")
	print ("-----")
	print ("MENÚ")
	print ("-----")
	print (""+B+"")
	print (" _ _ _ _ _ _ _ _ _ _")
	print ("|                   |")
	print ("| 1. A.Triangulo    |")
	print ("| 2. A.Rectangulo   |")
	print ("| 3. A.Cuadrado     |")
	print ("| 4. A.Rombo        |")
	print ("| 5. A.Romboide     |")
	print ("| 6. A.Trapecio     |")
	print ("| 7. Salir          |")
	print ("|_ _ _ _ _ _ _ _ _ _|")

	opcion = pedirOpcionCorrecta()

	if opcion == 1:
		os.system('clear')
		print ("A. Triangulo")
		b = int(input("La base es: "))
		h = int(input("La altura es: "))
		area_t = (b * h) / 2
		print (""+R+"")
		print ("El resultado es: ", area_t)
		time.sleep(6)
		os.system('clear')
	elif opcion == 2:
		os.system('clear')
		print ("A. Rectangulo")
		print ("Rectangulo")
		print (""+O+"")
		print ("""
		 __________________
		|                  |
		|                  | a
		|                  |
		|__________________|
			 b
		""")
		print (""+G+"")
		b = int(input("La base es: "))
		a = int(input("La altura es: "))
		area_r = a * b
		print (""+R+"")
		print ("El resultado es: ", area_r)
		time.sleep(6)
		os.system('clear')
	elif opcion == 3:
		os.system('clear')
		print ("A.Cuadrado")
		print ("Cuadrado")
		print (""+O+"")
		print ("""
		 ___________
		|           |
		|           | a
		|           |
		|___________|
		      a
		""")
		print (""+G+"")
		l = int(input("El Lado es: "))
		area_c = l ** 2
		print (""+R+"")
		print ("El resultado es: ", area_c)
		time.sleep(6)
		os.system('clear')
	elif opcion == 4:
		os.system('clear')
		print ("A.Rombo")
		D = int(input("La Diagonal mayor es: "))
		d = int(input("La diagonal menor es: "))
		area_ron = (D * d) / 2
		print (""+R+"")
		print ("El resultado es: ", area_ron)
		time.sleep(6)
		os.system('clear')
	elif opcion == 5:
		os.system('clear')
		print ("A.Romboide")
		print ("Romboide")
		print (""+O+"")
		print ("""
		    _ _ _ _ _ _ _ _
		   /|              /
		  / | h           /
		 /  |            /
		/_ _|_ _ _ _ _ _/
			B
		""")
		print (""+G+"")
		x = int(input("La base es: "))
		y = int(input("La altura es: "))
		area_rom = x * y
		print (""+R+"")
		print ("El resultado es: ", area_rom)
		time.sleep(6)
		os.system('clear')
	elif opcion == 6:
		os.system('clear')
		print ("A.Trapecio")
		print ("Trapecio")
		print (""+O+"")
		print ("""
		        b
		    _ _ _ _ _
		   /|        \
		  / |         \
		 /  | h        \
		/_ _|_ _ _ _ _ _\
		        B
		""")
		print (""+G+"")
		B = int(input("La Base mayor es: "))
		b = int(input("La base mayor es: "))
		h = int(input("La Altura es: "))
		area_tra = ((B + b) * h) / 2
		print (""+R+"")
		print ("El resultado es: ", area_tra)
		time.sleep(6)
		os.system('clear')
	elif opcion == 7:
		salir = True
	else:
		os.system('clear')
		print ("Introduce un numero entre 1 y 7")

print (""+R+"")
print ("¡Fín!, espero le haya gustado esta herranienta, hasta luego")
print ("")
