import telepot
import time
from picamera import PiCamera
from RPi.GPIO import *

setmode(BCM)
setup(18, IN)

photo = '/home/pi/Pictures/cammerabot.png'

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print(msg['chat']['username'])
    print('Got command: %s' % command)

    if command == '/start':
        bot.sendMessage(157833064, 'program successfully started')

    if command == '/photo':
        camera.capture(photo)
        bot.sendPhoto(157833064,open(photo,'rb'))

    if command == '/gaurdianon':
        bot.sendMessage(157833064, 'gurdian mode is ON')
        while 1:
            time.sleep(1)
            print(input(18))
            if input(18) == 1:
                camera.capture(photo)
                bot.sendPhoto(157833064,open(photo,'rb'))

            if command == '/gaurdianoff':
                bot.sendMessage(157833064, 'gaurdian mode is OFF')
                break

camera=PiCamera()
bot = telepot.Bot('568069486:AAHqf94nzFM9dkI3DhYaLMY6WI54dF8fUEg')
bot.message_loop(handle)
print('The code is running')

