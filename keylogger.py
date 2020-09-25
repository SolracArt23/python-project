import datetime
from pynput.keyboard import Listener # sirve para escuchar
def llave(key):
    print(key)

with Listener(on_press=llave) as l: # lo muest
    l.join()



