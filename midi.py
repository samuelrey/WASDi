import pyglet
from pyglet.window import key

window = pyglet.window.Window()

key_bindings = {
					'A':'Music/606/cassete 1/bd01.wav',
					'B':'Music/Game Boy/samples/arp01.wav',
					'C':'Music/DD-10/Samples/clap.wav'
				}

def play(letter):
	sample = pyglet.resource.media(key_bindings[letter], streaming=False)
	sample.play()

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.A:
		play('A')
	elif symbol == key.B:
		play('B')
	elif symbol == key.C:
		play('C')

@window.event
def on_draw():
	window.clear()

pyglet.app.run()
