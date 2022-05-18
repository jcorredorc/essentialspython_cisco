from sys import path
import os

path.append('..//packages')
dir = 'ruta absoluta la carpeta packages'
path.append(dir)
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(SCRIPT_DIR + "/packages")
# path.append(os.path.dirname(SCRIPT_DIR))
print(path)

# from ..packages import extra
import extra.iota

print(extra.iota.FunI())
