#!/usr/bin/python3

import os, sys, subprocess, yaml
from subprocess import call, run

#Borra los contenedores creados
subprocess.run(["sudo", "docker-compose", "down"])
#Borra las imagenes creadas
subprocess.run(["sudo", "docker", "rmi", "46/reviews", "46/ratings", "46/details", "46/productpage"])
