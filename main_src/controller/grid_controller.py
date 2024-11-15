import pygame
from model.settings import (GRID_SIZE, TILE_SIZE, PADDING_WIDTH, LEFT_MARGIN,
                            FLIP_DURATION)
from model.grid import Grid


class GridController:
    def __init__(self, image):
        # Initialize image and grid
        self.image = image if image is not None else self.create_placeholder_image()
        self.grid = Grid(PADDING_WIDTH, LEFT_MARGIN, self.image)

    def create_placeholder_image(self):
        placeholder_image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE // 2))
        placeholder_image.fill((255, 255, 255))
        return placeholder_image

    def handle_click(self, pos):
        # Adjust click position and determine row/col
        adjusted_x = pos[0] - self.grid.PADDING_WIDTH - self.grid.LEFT_MARGIN
        adjusted_y = pos[1]
        row, col = adjusted_y // TILE_SIZE, adjusted_x // TILE_SIZE

        # Ensure click is within grid bounds
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            tile = self.grid.tiles[row][col]
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
