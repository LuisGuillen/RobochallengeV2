import controlbluetooth as cbt
import time
from controlbluetooth import comando
cbt.iniciarBT()

while True:
    if cbt.bluetoothConectado.is_set():
        print("Comando recibido:",cbt.obtenerComando())
        time.sleep(0.5)