"""
Player state and movement.
"""
from typing import Tuple, Dict

PEE_THRESHOLD: int = 100

GridPos = Tuple[int, int]

class Player:
    def __init__(self, start: GridPos = (20,20)):
        self.y, self.x = start
        self.prev_position = None
        self.pee_counter = 0
        self.registered = False
        # degrees progress: name -> passes obtained
        self.degrees_progress: Dict[str, int] = {
            'audio_tech': 0,
            'culinary': 0,
            'network_ops': 0,
            'nursing': 0,
            'philosophy': 0,
        }

    def pos(self) -> GridPos:
        return (self.y, self.x)

    def move(self, dy: int, dx: int, map_width: int, map_height: int):
        
        ny = max(0, min(map_height - 1, self.y + dy))
        nx = max(0, min(map_width - 1, self.x + dx))
        moved = (ny != self.y) or (nx != self.x)
        self.y, self.x = ny, nx
        if moved:
            self.pee_counter += 1

    def undo_move(self):
        self.y, self.x = self.prev_position
    
    def need_to_pee(self) -> bool:
        return self.pee_counter >= PEE_THRESHOLD

    def reset_pee_counter(self):
        self.pee_counter = 0

    def register(self):
        self.registered = True

    def add_degree_pass(self, degree_name: str):
        if degree_name in self.degrees_progress:
            self.degrees_progress[degree_name] += 1

    def has_degree(self, degree_name: str, required_passes: int) -> bool:
        return self.degrees_progress.get(degree_name, 0) >= required_passes

    def all_degrees_earned(self, required_passes: int) -> bool:
        return all(self.has_degree(d, required_passes) for d in self.degrees_progress.keys())
