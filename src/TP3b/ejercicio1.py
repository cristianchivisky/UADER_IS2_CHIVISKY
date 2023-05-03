import platform
import subprocess
import os
from time import sleep

class Ping():

    def __init__(self):
        pass

    def execute(self, dir_ip) -> None:
        '''Ejecuta 10 intentos de ping a la dirección IP pasada como argumento,
        funciona solo si la dirección IP comienza con "192".'''
        print(f"el IP recibido es {dir_ip}")
        if dir_ip[: 3] == '192':
            if platform.system().lower() == 'windows':
                parametro = '-n'
            else:
                parametro = '-c'
            comando = ['ping', parametro, '1', dir_ip]
            for i in range(10):
                try:
                    subprocess.call(comando)
                    sleep(1)
                    print('\n')
                except :
                    print('No conectado')

    def executefree(self, dir_ip) -> None:
        '''Ejecuta lo mismo que el método execute pero sin el control de dirección'''
        if platform.system().lower() == 'windows':
            parametro = '-n'
        else:
            parametro = '-c'
        comando = ['ping', parametro, '1', dir_ip]
        for i in range(10):
            try:
                subprocess.call(comando)
                sleep(1)
                print('\n')
            except:
                print('No conectado')

class PingProxi():
    def __init__(self) -> None:
        self._klass = Ping()

    def execute(self, dir_ip) -> None:
        '''Si la dirección IP es 192.168.0.254 realiza un ping a "www.Google.com",
        usando el método "executefree" de la clase Ping, en cualquier otro caso reenvia a "execute" de la clase Ping.'''
        if dir_ip == '192.168.0.254':
            new_ip = 'www.google.com'
            print(f"la clave recibida por el proxi es {dir_ip} la enviada es {new_ip}")
            self._klass.executefree(new_ip)
        else:
            self._klass.execute(dir_ip)


#*------------------------------------------------------------
#* main
#*------------------------------------------------------------

os.system("clear")

#*-- Crea objeto proxy
secured_ping = PingProxi()
IP = '192.168.1.1'
secured_ping.execute(IP)
IP = '192.168.0.254'
secured_ping.execute(IP)
