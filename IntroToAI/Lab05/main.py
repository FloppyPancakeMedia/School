"""
Entry point for the terminal college game.
"""
import curses

from game.game import Game


def fail(stdscr, message: str):
    stdscr.clear()
    stdscr.addstr(0,0, message)
    stdscr.addstr(2,0, "Press any key to quit.")
    stdscr.refresh()
    stdscr.getch()

def start(stdscr):
    game = Game(stdscr)
    is_okay = game.check_screen(stdscr)
    if is_okay != "":
        fail(stdscr, is_okay)
    game.game_loop(stdscr, "Play ball")

if __name__ == '__main__':
    curses.wrapper(start)
