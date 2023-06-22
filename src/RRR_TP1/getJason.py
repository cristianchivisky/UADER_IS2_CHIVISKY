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

if __debug__ :
    print('__debug__ is True --> codigo nuevo\n')
else :
    print('__debug__ is False --> codigo viejo\n')

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class APItoken(metaclass=SingletonMeta):
    def __init__(self):
        pass

    def extraer_token(self, jsonfile, jsonkey):
        try:
            with open(jsonfile, 'r') as myfile:
                data = myfile.read()
        except FileNotFoundError:
            print('No existe el archivo JSON')
            sys.exit()
        except ValueError:
            print('Error al cargar el archivo JSON')
            sys.exit()
        try:
            obj = json.loads(data)
            print(str(obj[jsonkey]))
        except KeyError:
            print('Token incorrecto, no existe en el archivo JSON')
            sys.exit()
        except:
            print('Error al extraer el token del archivo JSON')
            sys.exit()

    def obtener_mensaje_ayuda(self):
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

def obtener_mensaje_ayuda_viejo():
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

def extraer_token_viejo(jsonfile, jsonkey):
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

class abstarctExtractorToken:
    def __init__(self):
        self.p1=APItoken()
    
    def extraer_token(self, jsonfile, jsonkey):
        if __debug__:
            self.p1.extraer_token(jsonfile, jsonkey)
        else:
            extraer_token_viejo(jsonfile, jsonkey)

    def obtener_mensaje_ayuda(self):
        if __debug__:
            self.p1.obtener_mensaje_ayuda()
        else:
            obtener_mensaje_ayuda_viejo()


#*--------------------------------------------------------------
# main
#*--------------------------------------------------------------
z1=abstarctExtractorToken()
try:
    if sys.argv[1] == '-h':
        z1.obtener_mensaje_ayuda()
    else:
        jsonfile = sys.argv[1]
        jsonkey = sys.argv[2]
        z1.extraer_token(jsonfile, jsonkey)
except IndexError:
    print('Argumento invalido')
    sys.exit()

# okay decompiling getJason.pyc