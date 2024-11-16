import random
from model.tile import Tile
from model.settings import GRID_SIZE, TILE_SIZE, BORDER_WIDTH, \
    STATS_AREA_HEIGHT, TILE_TOTAL_SIZE, WHITESPACE


class Grid:
    def __init__(self, image):
        self.tiles = []
        self.revealed_tiles = []
        self.image = image
        self.generate_tiles()

    def generate_tiles(self):
        num_pairs = (GRID_SIZE * GRID_SIZE) // 2
        tile_types = [i for i in range(num_pairs)] * 2
        random.shuffle(tile_types)

        # Generate unique colors for each pair
        unique_colors = [(random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255)) for _ in range(num_pairs)]
        color_map = {tile_type: unique_colors[tile_type] for tile_type in range(num_pairs)}

        for row in range(GRID_SIZE):
            row_tiles = []
            for col in range(GRID_SIZE):
                tile_type = tile_types.pop()

                # Calculate tile position using TILE_TOTAL_SIZE
                x = WHITESPACE + col * TILE_TOTAL_SIZE
                y = WHITESPACE + row * TILE_TOTAL_SIZE + STATS_AREA_HEIGHT

                # Try to create the Tile instance
                try:
                    tile = Tile(tile_type, color_map[tile_type], x, y, self.image)
                except Exception as e:
                    raise RuntimeError(f"Failed to create Tile with type {tile_type} at position ({x}, {y}): {e}")

                # Append the successfully created tile to the row
                row_tiles.append(tile)

            self.tiles.append(row_tiles)

    def draw(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)

    def all_matched(self):
        return all(tile.matched for row in self.tiles for tile in row)
