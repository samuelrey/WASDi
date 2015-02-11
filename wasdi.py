import pyglet
from pyglet.window import key

window = pyglet.window.Window()

key_bindings = {
					'SPACE':'Music/606/clean/bd01.wav',
					'W':'Music/606/cassete 1/sn06.wav',
					'A':'Music/Game Boy/sfx07.wav',
					'S':'Music/606/clean/ch12.wav',
					'D':'Music/Game Boy/arp01.wav'
				}

def play(letter):
	sample = pyglet.resource.media(key_bindings[letter], streaming=False)
	sample.play()

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.W:
		play('W')
	elif symbol == key.A:
		play('A')
	elif symbol == key.S:
		play('S')
	elif symbol == key.D:
		play('D')
	elif symbol == key.SPACE:
		play('SPACE')

@window.event
def on_draw():
	window.clear()

pyglet.app.run()
