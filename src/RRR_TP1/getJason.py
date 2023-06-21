#*-----------------------------------------------------------------------------------
#getJason
#Este programa permite extraer la clave de acceso API para utilizar los servicios del Banco xxx.
#Este programa esta siendo obtenido por ingenieria reversa el 15/06/2023.
#*-----------------------------------------------------------------------------------
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
#*-----------------------------------------------------------------------------------
import json, sys
try:
    if sys.argv[1] == '-h':
        print('Mensaje de ayuda:')
        print('  Extractor de token para acceso API Servicios Banco XXX (version 1.0)\n')
        print('  Este programa permite extraer la clave de acceso API para utilizar los servicios del Banco XXX.\n')
        print('  El programa operara como un microservicio invocado mediante:')
        print('  {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json')
        print('  Ejemplo:')
        print('  ./getJason.pyc ./sitedata.json\n')
        print('  El token podra recuperarse mediante el standard output de ejecucion en el formato')
        print('  XXXX-XXXX-XXXX-XXXX')
        sys.exit()
    else:
        jsonfile = sys.argv[1]
        jsonkey = sys.argv[2]
except IndexError:
    print('Argumento invalido')
    sys.exit()

try:
    with open(jsonfile, 'r') as (myfile):
        data = myfile.read()
except FileNotFoundError:
    print('No existe el archivo JSON')
    sys.exit()
except ValueError:
    print('Error al cargar el archivo JSON')
    sys.exit()

try:
    obj = json.loads(data)
    print (str(obj[jsonkey]))
except KeyError:
    print('Token incorrecto, no existe en el archivo JSON')
    sys.exit()
except:
    print('Error al extraer el token del archivo JSON')
    sys.exit()

# okay decompiling getJason.pyc
