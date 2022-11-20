from pynput import *
def gc(x, y):
    print("C : {}".format((x, y)))
with mouse.Listener(on_move = gc) as listen:
          listen.join()
