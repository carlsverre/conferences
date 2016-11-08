import curses
import time

screen = curses.initscr()

curses.noecho()
curses.curs_set(0)
screen.keypad(1)
screen.nodelay(1)

i = 0

while True:
    i += 1

    event = screen.getch()
    screen.clear()

    if event == ord("q"):
        break

    elif event == curses.KEY_F2:
        screen.addstr("The User Pressed F2", curses.A_BLINK)
        screen.refresh()

    else:
        screen.addstr("Loop {0}".format(i))

curses.endwin()
