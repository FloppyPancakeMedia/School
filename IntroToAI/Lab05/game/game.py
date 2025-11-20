import curses
import time

import game.buildings as buildings
from game.map import Map
from game.player import Player
from game.ui import UI
from services import gemini_client

PASSES_REQUIRED_PER_DEGREE = 2



DEGREE_BUILDINGS = {'audio_tech','culinary','network_ops','nursing','philosophy'}

USING_GEMINI: bool = True

class Game:
    def __init__(self, stdscr):
        self.game_map: Map = Map()
        self.player: Player = Player(start=(20,20))
        self.ui: UI = UI(stdscr, self.game_map)
        self.client = gemini_client.get_client(USING_GEMINI)

    def check_screen(self, stdscr) -> bool:
        # verify terminal is large enough to render the map
        max_y, max_x = stdscr.getmaxyx()
        min_height = self.game_map.HEIGHT + self.ui.height_offset + 2
        min_width = self.game_map.WIDTH
        # Terminate if not large enough
        if max_y < min_height or max_x < min_width:
            message = f"Terminal too small: need at least {min_width}x{min_height}. Resize and try again."
            return message

        return ""
    
    def game_loop(self, stdscr, message):
        message = 'Welcome! Walk to `admin` to register before attempting degrees.'
        self.ui.render(self.player.pos(), message)

        while True:
            
            # self.ui.show_message(message)
            ch = stdscr.getch()
            if ch == ord('q'):
                break
            dy = dx = 0
            if ch == curses.KEY_UP:
                dy = -1
            elif ch == curses.KEY_DOWN:
                dy = 1
            elif ch == curses.KEY_LEFT:
                dx = -1
            elif ch == curses.KEY_RIGHT:
                dx = 1
            else:
                # ignore other keys
                continue

            # check pee requirement
            if self.player.need_to_pee():
                message = 'You really need to visit the bathroom. Go there now!'
                # allow movement but if not at bathroom, block degree attempts
                # self.player.move(dy, dx, self.game_map.WIDTH, self.game_map.HEIGHT)
                # if stepped into bathroom, handle below
            
            old_pos = self.player.pos()
            self.player.move(dy, dx, self.game_map.WIDTH, self.game_map.HEIGHT)

            pos = self.player.pos()
            b = self.game_map.building_at(pos)
            if b:
                # trigger interaction
                if b == 'bathroom':
                    message = buildings.bathroom(pos, self.ui, self.player, self.client)
            
                if self.player.need_to_pee():
                    message = "You might pee yourself if you go here... You should probably fix that"
                else:
                    if b == 'admin' and not self.player.registered:
                        message = buildings.admin(pos, self.ui, self.player, self.client)

                    # degree buildings
                    if b in DEGREE_BUILDINGS:
                        message = buildings.degree_building(pos, b, self.ui, self.player, self.game_map, self.client)

                        if self.player.has_degree(b, PASSES_REQUIRED_PER_DEGREE):
                            message += f" You earned the {self.game_map.display_names[b]} degree!"

                    # win check
                    if self.player.all_degrees_earned(PASSES_REQUIRED_PER_DEGREE):
                        self.ui.render(self.player.pos(), 'Congratulations! You earned all degrees and won! Press q to qself.uit.')
                        stdscr.getch()
                        break
                self.player.undo_move()
            
            self.player.prev_position = old_pos
                
            self.ui.render(pos)
            self.ui.show_message(message)
            # self.player.prev_position = pos
            # small throttle
            time.sleep(0.03)