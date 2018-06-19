from pynput import *

def on_press(key):
    print('key{} pressed'.format(key))
def on_relase(key):
    print('key{} realsed'.format(key))
    
with keyboard.Listener(on_press=on_press, on_relase=on_relase) as listener:
    listener.join()
