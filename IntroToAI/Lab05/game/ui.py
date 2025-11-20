"""
Curses UI for the game: renders map, buildings as '*' squares, player as '@', and a message/input box below the map.
"""
import curses
from typing import Tuple, Optional
import textwrap
from game.map import Map

class UI:
    def __init__(self, stdscr, game_map: Map, height_offset: int = 5):
        self.stdscr = stdscr
        self.map = game_map
        self.height_offset = height_offset
        curses.curs_set(0)
        self.stdscr.nodelay(False)
        self.stdscr.keypad(True)

    def render(self, player_pos: Tuple[int,int], message: Optional[str] = None):
        self.stdscr.erase()
        max_y, max_x = self.stdscr.getmaxyx()
        draw_height = min(self.map.HEIGHT, max_y - self.height_offset - 1)
        draw_width = min(self.map.WIDTH, max_x)

        # Draw the map area
        for y in range(draw_height):
            for x in range(draw_width):
                ch = ' '
                if (y,x) == player_pos:
                    ch = '@'
                elif self.map.is_building_tile((y,x)):
                    ch = '*'
                try:
                    self.stdscr.addch(y, x, ch)
                except curses.error:
                    pass

        # Draw the message box area below the map
        base = draw_height + 1
        try:
            self.stdscr.hline(draw_height, 0, '-', draw_width)
        except curses.error:
            pass

        if message != None:
            # Wrap the message text to fit within the screen width
            wrapped_message = textwrap.wrap(message, width=draw_width)
            for i, line in enumerate(wrapped_message):
                if base + i >= max_y - 1:  # Prevent overflow
                    break
                try:
                    self.stdscr.addstr(base + i, 0, line[:draw_width])
                except curses.error:
                    pass

        self.stdscr.refresh()


    def show_message(self, message: str) -> tuple[int, int]:
        if message is None:
            message = ""
        
        max_y, max_x = self.stdscr.getmaxyx()
        draw_height = min(self.map.HEIGHT, max_y - self.height_offset - 1)
        draw_width = min(self.map.WIDTH, max_x)
        base = draw_height + 1

        wrapped = textwrap.wrap(message, width=draw_width)
        for i, line in enumerate(wrapped):
            row = base + i
            if row >= max_y - 1:
                break
            try:
                self.stdscr.addstr(row, 0, line.ljust(draw_width)[:draw_width])
            except curses.error:
                pass
        self.stdscr.refresh()
        return base + len(wrapped), draw_width
    
    def show_paged_message(self, message: str) -> None:
        """
        Fullscreen pager for long messages. Navigation:
            space/Right/Down/PageDown -> next page
            Left/Up/b/PageUp         -> prev page
            q or ESC                 -> exit pager
        """
        if message is None:
            message = ""
        max_y, max_x = self.stdscr.getmaxyx()
        draw_width = min(self.map.WIDTH, max_x)

        wrapped = textwrap.wrap(message, width=draw_width)
        page_height = max(1, max_y - 2)  # leave one line for controls
        total_pages = (len(wrapped) + page_height - 1) // page_height
        page = 0

        try:
            curses.curs_set(0)
        except Exception:
            pass

        while True:
            self.stdscr.erase()
            start = page * page_height
            end = min(start + page_height, len(wrapped))
            for i, line in enumerate(wrapped[start:end]):
                try:
                    self.stdscr.addstr(i, 0, line[:draw_width])
                except curses.error:
                    pass

            status = f"[Page {page+1}/{max(1,total_pages)}] space/→/↓ next, ←/↑/b prev, q quit"
            try:
                self.stdscr.addstr(max_y - 1, 0, status[:max_x - 1])
            except curses.error:
                pass
            self.stdscr.refresh()

            try:
                ch = self.stdscr.get_wch()
            except curses.error:
                break

            # quit
            if isinstance(ch, str) and ch.lower() == 'q':
                break
            if ch == '\x1b':  # ESC
                break

            # next page
            if (isinstance(ch, str) and ch == ' ') or ch in (curses.KEY_RIGHT, curses.KEY_DOWN, curses.KEY_NPAGE):
                if page < total_pages - 1:
                    page += 1
                else:
                    break
                continue

            # prev page
            if (isinstance(ch, str) and ch.lower() == 'b') or ch in (curses.KEY_LEFT, curses.KEY_UP, curses.KEY_PPAGE):
                if page > 0:
                    page -= 1
                continue

        # caller should re-render map after pager exits
        return

    def prompt_input(self, prompt: str) -> str:
        """
        Automatically pages the prompt if it doesn't fit the message area,
        then displays the prompt in the message area and accepts wrapped input.
        """
        # compute layout params
        max_y, max_x = self.stdscr.getmaxyx()
        draw_height = min(self.map.HEIGHT, max_y - self.height_offset - 1)
        draw_width = min(self.map.WIDTH, max_x)
        base = draw_height + 1

        # prepare wrapped prompt and decide if we need a pager
        if prompt is None:
            prompt = ""
        wrapped_prompt = textwrap.wrap(prompt, width=draw_width)
        available_message_rows = max(0, max_y - base - 1)  # leave one line at bottom

        if len(wrapped_prompt) > available_message_rows:
            # show pager so user can read full prompt, then redraw top of prompt
            self.show_paged_message(prompt)
            # after pager, re-render the top portion into the message box
            self.show_message(prompt)

        # draw prompt (ensures message is present and returns input row)
        input_row, draw_width = self.show_message(prompt)
        max_y, _ = self.stdscr.getmaxyx()
        buffer: list[str] = []
        pos = 0

        curses.noecho()
        try:
            curses.curs_set(1)
        except Exception:
            pass

        try:
            while True:
                # clear only the input area (leave prompt intact)
                for r in range(input_row, max_y):
                    try:
                        self.stdscr.move(r, 0)
                        self.stdscr.clrtoeol()
                    except curses.error:
                        pass

                text = ''.join(buffer)
                wrapped = textwrap.wrap(text, width=draw_width) if text else ['']
                for i, line in enumerate(wrapped):
                    row = input_row + i
                    if row >= max_y - 1:
                        break
                    try:
                        self.stdscr.addstr(row, 0, line.ljust(draw_width)[:draw_width])
                    except curses.error:
                        pass

                before = text[:pos]
                before_wrapped = textwrap.wrap(before, width=draw_width) if before else ['']
                cur_row = input_row + len(before_wrapped) - 1
                cur_col = len(before_wrapped[-1]) if before_wrapped else 0
                cur_row = min(cur_row, max_y - 2)
                cur_col = min(cur_col, draw_width - 1)
                try:
                    self.stdscr.move(cur_row, cur_col)
                except curses.error:
                    pass

                ch = self.stdscr.get_wch()
                if isinstance(ch, str):
                    if ch in ('\n', '\r'):
                        break
                    if ch in ('\x08', '\x7f'):
                        if pos > 0:
                            del buffer[pos - 1]
                            pos -= 1
                    else:
                        buffer.insert(pos, ch)
                        pos += 1
                else:
                    if ch == curses.KEY_LEFT and pos > 0:
                        pos -= 1
                    elif ch == curses.KEY_RIGHT and pos < len(buffer):
                        pos += 1
                    elif ch in (curses.KEY_BACKSPACE, 127) and pos > 0:
                        del buffer[pos - 1]
                        pos -= 1
                    elif ch == curses.KEY_DC and pos < len(buffer):
                        del buffer[pos]

        finally:
            curses.echo()
            try:
                curses.curs_set(0)
            except Exception:
                pass

        return ''.join(buffer).strip()

    # def prompt_input(self, prompt: str) -> str:
    #     input_row, draw_width = self.show_message(prompt)
    #     max_y, _ = self.stdscr.getmaxyx()
    #     buffer: list[str] = []
    #     pos = 0

    #     curses.noecho()
    #     curses.curs_set(1)
    #     try:
    #         while True:
    #             # clear only the input area
    #             for r in range(input_row, max_y):
    #                 try:
    #                     self.stdscr.move(r, 0)
    #                     self.stdscr.clrtoeol()
    #                 except curses.error:
    #                     pass

    #             text = ''.join(buffer)
    #             wrapped = textwrap.wrap(text, width=draw_width) if text else ['']
    #             for i, line in enumerate(wrapped):
    #                 row = input_row + i
    #                 if row >= max_y - 1:
    #                     break
    #                 try:
    #                     self.stdscr.addstr(row, 0, line.ljust(draw_width)[:draw_width])
    #                 except curses.error:
    #                     pass

    #             before = text[:pos]
    #             before_wrapped = textwrap.wrap(before, width=draw_width) if before else ['']
    #             cur_row = input_row + len(before_wrapped) - 1
    #             cur_col = len(before_wrapped[-1]) if before_wrapped else 0
    #             cur_row = min(cur_row, max_y - 2)
    #             cur_col = min(cur_col, draw_width - 1)
    #             try:
    #                 self.stdscr.move(cur_row, cur_col)
    #             except curses.error:
    #                 pass

    #             ch = self.stdscr.get_wch()
    #             if isinstance(ch, str):
    #                 if ch in ('\n', '\r'):
    #                     break
    #                 if ch in ('\x08', '\x7f'):
    #                     if pos > 0:
    #                         del buffer[pos - 1]
    #                         pos -= 1
    #                 else:
    #                     buffer.insert(pos, ch)
    #                     pos += 1
    #             else:
    #                 if ch == curses.KEY_LEFT and pos > 0:
    #                     pos -= 1
    #                 elif ch == curses.KEY_RIGHT and pos < len(buffer):
    #                     pos += 1
    #                 elif ch in (curses.KEY_BACKSPACE, 127) and pos > 0:
    #                     del buffer[pos - 1]
    #                     pos -= 1
    #                 elif ch == curses.KEY_DC and pos < len(buffer):
    #                     del buffer[pos]

    #     finally:
    #         curses.echo()
    #         curses.curs_set(0)

    #     return ''.join(buffer).strip()

    # def prompt_input(self, prompt: str) -> str:
    #     # show prompt in the message area and accept a full-line input
    #     curses.echo()
    #     max_y, max_x = self.stdscr.getmaxyx()
    #     draw_height = min(self.map.HEIGHT, max_y - self.height_offset - 1)
    #     draw_width = min(self.map.WIDTH, max_x)
    #     base = draw_height + 4

    #     wrapped_prompt = textwrap.wrap(prompt, width=draw_width)
    #     try:
    #         for i, line in enumerate(wrapped_prompt):
    #             if base + i >= max_y - 1:
    #                 break
    #             self.stdscr.addstr(base + i, 0, line[:draw_width])

    #         self.stdscr.clrtoeol()
    #         self.stdscr.refresh()
    #         curses.curs_set(1)
    #         curses.cbreak()

    #         # fall back to stdscr.getstr so we don't create windows that may not fit
    #         inp = self.stdscr.getstr(base + len(wrapped_prompt), 0, draw_width - 1).decode('utf-8')
    #     except curses.error:
    #         # if any curses error occurs, return empty response
    #         inp = ''
    #     curses.noecho()
    #     curses.curs_set(0)
    #     return inp
