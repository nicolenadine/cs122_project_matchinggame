import pygame
from model.settings import (GRID_SIZE, TILE_SIZE, BORDER_WIDTH,
                            STATS_AREA_HEIGHT, FLIP_DURATION)
from model.grid import Grid


class GridController:
    def __init__(self, image):
        # Initialize image and grid
        self.image = image if image is not None else self.create_placeholder_image()
        self.grid = Grid(self.image)

    def create_placeholder_image(self):
        placeholder_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        placeholder_image.fill((255, 255, 255))
        return placeholder_image

    def handle_click(self, pos):
        # Adjust click position to account for border and stats area
        adjusted_x = pos[0] // (TILE_SIZE + 2 * BORDER_WIDTH)
        adjusted_y = (pos[1] - STATS_AREA_HEIGHT) // (TILE_SIZE + 2 * BORDER_WIDTH)

        print(
            f"Click at ({pos[0]}, {pos[1]}) adjusted to ({adjusted_x}, {adjusted_y}), row: {adjusted_y}, col: {adjusted_x}")

        # Ensure click is within grid bounds
        if 0 <= adjusted_y < GRID_SIZE and 0 <= adjusted_x < GRID_SIZE:
            tile = self.grid.tiles[adjusted_y][adjusted_x]
            if not tile.matched and not tile.flipped:
                tile.flipped = True
                self.grid.revealed_tiles.append(tile)

    def process_tile_selection(self):
        if len(self.grid.revealed_tiles) == 2:
            tile1, tile2 = self.grid.revealed_tiles
            if tile1.tile_type == tile2.tile_type:
                tile1.matched = True
                tile2.matched = True
            else:
                pygame.time.delay(int(FLIP_DURATION * 1000))
                tile1.flipped = False
                tile2.flipped = False
            self.grid.revealed_tiles.clear()

    def draw(self, screen):
        self.grid.draw(screen)

    def all_matched(self):
        return self.grid.all_matched()
