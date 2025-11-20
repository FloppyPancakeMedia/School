"""
Map for the 40x40 campus. Buildings are represented as 3x3 squares of '*' characters.
This module exposes a Map class with building positions and helper methods.
"""
from typing import Dict, List, Tuple

GridPos = Tuple[int, int]

class Map:
    WIDTH = 40
    HEIGHT = 20
    BUILDING_SIZE = 3  # 3x3 blocks

    def __init__(self):
        # buildings -> list of (y,x) tiles
        self.buildings: Dict[str, List[GridPos]] = {}
        self._create_buildings()

    def _square_tiles(self, top: GridPos) -> List[GridPos]:
        y0, x0 = top
        tiles = []
        for dy in range(self.BUILDING_SIZE):
            for dx in range(self.BUILDING_SIZE):
                tiles.append((y0 + dy, x0 + dx))
        return tiles

    def _create_buildings(self):
        # corners
        self.buildings['admin'] = self._square_tiles((1,1))
        self.buildings['bathroom'] = self._square_tiles((1, self.WIDTH - self.BUILDING_SIZE - 1))
        self.buildings['audio_tech'] = self._square_tiles((self.HEIGHT - self.BUILDING_SIZE - 1, 1))
        self.buildings['culinary'] = self._square_tiles((self.HEIGHT - self.BUILDING_SIZE - 1, self.WIDTH - self.BUILDING_SIZE - 1))

        # interior degree buildings (place roughly in the middle)
        self.buildings['network_ops'] = self._square_tiles((10, 10))
        self.buildings['nursing'] = self._square_tiles((10, 26))
        self.buildings['philosophy'] = self._square_tiles((26, 10))

        # Map of display names
        self.display_names = {
            'admin': 'Admin',
            'bathroom': 'Bathroom',
            'audio_tech': 'Audio Tech',
            'culinary': 'Culinary',
            'network_ops': 'Network Ops',
            'nursing': 'Nursing',
            'philosophy': 'Philosophy',
        }

    def is_building_tile(self, pos: GridPos) -> bool:
        for tiles in self.buildings.values():
            if pos in tiles:
                return True
        return False

    def building_at(self, pos: GridPos) -> str | None:
        possible_positions = [self.add_pos(pos, (1, 0)), self.add_pos(pos, (0, 1)), self.add_pos(pos, (-1, 0)), self.add_pos(pos, (0, -1))]
        for name, tiles in self.buildings.items():
            for pos in possible_positions:
                if pos in tiles:
                    return name
        return None

    def building_center(self, name: str) -> GridPos:
        tiles = self.buildings[name]
        # return the center tile
        return tiles[len(tiles)//2]

    def all_buildings(self) -> List[str]:
        return list(self.buildings.keys())

    def add_pos(self, pos1, pos2) -> GridPos:
        return (pos1[0] + pos2[0], pos1[1] + pos2[1])