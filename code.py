
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import audioio
import audiocore
import neopixel
from colorpallette import colors

#Audio Files
thanks = "thank you2.wav"
h = "h2.wav"
bad = "bad2.wav"
good = "g2.wav"
done = "done.wav"
more = "more2.wav"

# Button pins:
a = DigitalInOut(board.A4)
a.direction = Direction.INPUT
a.pull = Pull.UP

b = DigitalInOut(board.A5)
b.direction = Direction.INPUT
b.pull = Pull.UP

c = DigitalInOut(board.A6)
c.direction = Direction.INPUT
c.pull = Pull.UP

d = DigitalInOut(board.A7)
d.direction = Direction.INPUT
d.pull = Pull.UP

e = DigitalInOut(board.A2)
e.direction = Direction.INPUT
e.pull = Pull.UP

f = DigitalInOut(board.A3)
f.direction = Direction.INPUT
f.pull = Pull.UP

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1)


#Color Pallete import
col = [
    colors.RED,
    colors.GREEN,
    colors.MINT,
    colors.BLUE,
    colors.CYAN,
    colors.NEON,
    colors.CYBER,
    colors.MAGENTA,
    colors.ORANGE,
]

# Audio Play File
def play_file(playname, x):
    print("Playing File " + playname)
    wave_file = open(playname, "rb")
    with audiocore.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                for i in range(len(pixels)):
                    pixels[i] = col[x]
                    time.sleep(0.1)
                pixels.fill(0)
                time.sleep(0.3)
                pixels.show()


while True:
    if not a.value:
        play_file(thanks,6)
    if not b.value:
        play_file(h,8)
    if not c.value:
        play_file(bad,0)
    if not d.value:
        play_file(good,1)
    if not e.value:
        play_file(done,4)
    if not f.value:
        play_file(more,5)
