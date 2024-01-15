#!/usr/bin/python3

import os, sys, subprocess, yaml
from subprocess import call, run

#Borra el contenedor creado
subprocess.run(["sudo", "docker", "rm", "g46-productpage"])
#Borra la imagen creada
subprocess.run(["sudo", "docker", "rmi", "g46/product-page"])
