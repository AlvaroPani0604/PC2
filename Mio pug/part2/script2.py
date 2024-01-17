#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call

#Instalar paquetes
subprocess.run(["sudo", "apt-get" ,"install","git", "-y"])
subprocess.run(["sudo", "apt" ,"update"])
subprocess.run(["sudo", "apt" ,"upgrade", "-y"])
subprocess.run(["sudo", "apt" ,"install", "docker-compose", "-y"])

#Construimos la imagen de docker 
subprocess.run(["sudo", "docker" ,"build", "-t", "g46/product-page", "."])

#Arrancamos el contenedor de docker
subprocess.run(["sudo", "docker", "run", "--name", "g46-productpage","-p9080:9080","g46/product-page"])
