#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call

#Funcion remp para reemplazar dentro de un rempivo de practica_creativa2
def remp(fi, remp1, remp2):
	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'r')

	with fin as file:
		x= file.read()
	fin.close()

	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'w')
	with fin as file:
		x= x.replace(remp1, remp2)
		fin.write(x)
	fin.close()

#Clonamos la carpeta practica_creativa2 del github
subprocess.run(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2"])

#Modificaciones del fichero requirements.txt con la funcion anterior
remp('requirements.txt', 'urllib3==1.26.5', 'urllib3')
remp('requirements.txt', 'chardet==3.0.4', 'chardet')
remp('requirements.txt', 'gevent==1.4.0', 'gevent')
remp('requirements.txt', 'greenlet==0.4.15', 'greenlet')

#Instalamos pip sudo apt-get install python-pip
subprocess.run(["sudo", "apt-get", "install", "python3-pip"])

#Instalamos dependencias de requirements.txt con pip
subprocess.run(["pip3", "install", '-r', './practica_creativa2/bookinfo/src/productpage/requirements.txt'])

#Creamos la variable de entorno (con nuestro num de grupo, 46)

os.environ['GRUPO_NUMERO']= "46"

#Extraemos la variable de entorno y guardarla aqui
title = os.environ.get('GRUPO_NUMERO')

#Modificamos productpage.html para cambiar el titulo de la app por la variable de entorno
remp('templates/productpage.html', 'Simple Bookstore App', title)

# Modificamos el script productpage_monolith.py para cambiar el puerto por defecto (9080)
remp('productpage_monolith.py', '9080', '9080')

# Llamamos a productpage_monolith.py para crear la aplicacion (como si fuese un monolito)
subprocess.run(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", '9080'])
