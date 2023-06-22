"""Copyright IS2 © 2022, 2023 todos los derechos reservados."""
#*----------------------------------------------------------------------------------
#getJason
#Este programa permite extraer la clave de acceso API para utilizar los servicios del Banco xxx.
#Este programa esta siendo obtenido por ingenieria reversa el 15/06/2023.
#*-----------------------------------------------------------------------------------
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18)
# [MSC v.1900 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
#*-----------------------------------------------------------------------------------
import json
import sys

class SingletonMeta(type):
    """Clase que implementa el patron Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Este metodo se llama cuando se crea una instancia de la clase APItoken."""
        if cls not in cls._instances:
            # Si no existe una instancia previa de la clase, se crea una nueva
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance# Se guarda la instancia creada
        return cls._instances[cls]  # Se devuelve la instancia almacenada en _instances

class APItoken(metaclass=SingletonMeta):
    """Esta clase implementa la logica para extraer un token
      de un archivo JSON y mostrar un mensaje de ayuda."""
    def __init__(self):
        """Este metodo se ejecuta al crear una instancia de la clase"""

    def extraer_token(self, jsonfile, jsonkey):
        """Este metodo permite extraer un token de un archivo JSON."""
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
        """Este metodo imprime un mensaje de ayuda en la consola."""
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

#*--------------------------------------------------------------
# main
#*--------------------------------------------------------------
if __name__ == "__main__":

    z1=APItoken() # Se crea una instancia de la clase APItoken
    try:
        if sys.argv[1] == '-h':
            z1.obtener_mensaje_ayuda()
        else:
            JSONFILE = sys.argv[1] # Se obtienen los nombres de archivo JSON
            JSONKEY = sys.argv[2] #y clave desde los argumentos de linea de comandos
            z1.extraer_token(JSONFILE, JSONKEY)
    except IndexError:
        print('Argumento invalido')
        sys.exit()
        # Si se produce un error de indice en los argumentos de linea de comandos,
        #  muestra un mensaje de error y se sale del programa

# okay decompiling getJason.pyc
