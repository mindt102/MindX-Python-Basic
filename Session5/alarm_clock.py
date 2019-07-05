import pyglet
import datetime

music = pyglet.resource.media('duck_quack.wav',streaming = False)

while True:
    date = datetime.datetime.now()
    if date.hour <21:
        music.play()
        break

    
    