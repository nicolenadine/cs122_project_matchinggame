import random
from model.tile import Tile
from model.settings import GRID_SIZE, TILE_SIZE


class Grid:
    def __init__(self, padding_width, left_margin, image):
        self.tiles = []
        self.revealed_tiles = []
        self.moves = 0
        self.PADDING_WIDTH = padding_width
        self.LEFT_MARGIN = left_margin
        self.image = image
        self.generate_tiles()


    def generate_tiles(self):
        num_pairs = (GRID_SIZE * GRID_SIZE) // 2
        tile_types = [i for i in range(num_pairs)] * 2
        random.shuffle(tile_types)

        # Generate unique colors for each pair
        unique_colors = [(random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255)) for _ in range(num_pairs)]
        color_map = {tile_type: unique_colors[tile_type] for tile_type in
                     range(num_pairs)}
        for row in range(GRID_SIZE):
            row_tiles = []
            for col in range(GRID_SIZE):
                tile_type = tile_types.pop()
                x = self.PADDING_WIDTH + self.LEFT_MARGIN + col * TILE_SIZE  #
                # Adjust x position for padding and margin
                y = row * TILE_SIZE
                row_tiles.append(Tile(tile_type, color_map[tile_type], x, y,
                                      self.image),)
            self.tiles.append(row_tiles)

    def draw(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)

    def all_matched(self):
        return all(tile.matched for row in self.tiles for tile in row)
