import pygame
from model.settings import GRID_SIZE, TILE_SIZE, FLIP_DURATION, \
    PADDING_WIDTH, LEFT_MARGIN, get_image
from model.grid import Grid


class GridController:
    def __init__(self, image):
        # Ensure image is an instance of suface
        if image is None:
            print(
                "Warning: No valid image provided, using a placeholder surface.")
            # Create a default/fallback surface (e.g., a blank tile)
            self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE // 2))
            self.image.fill((255, 255,
                             255))  # Placeholder color
        else:
            self.image = image
        self.grid = Grid(PADDING_WIDTH, LEFT_MARGIN, self.image)

    def handle_click(self, pos):
        # Adjust click position by subtracting the padding and margin
        adjusted_x = pos[0] - self.grid.PADDING_WIDTH - self.grid.LEFT_MARGIN
        adjusted_y = pos[1]
        row, col = adjusted_y // TILE_SIZE, adjusted_x // TILE_SIZE

        # Ensure click is within grid bounds
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            tile = self.grid.tiles[row][col]
            if not tile.matched and not tile.flipped:
                tile.flipped = True
                self.grid.revealed_tiles.append(tile)

                # Check for match if two tiles are revealed
                if len(self.grid.revealed_tiles) == 2:
                    self.grid.moves += 1
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
        self.grid.draw(screen)  # Delegate drawing to the Grid object

    def all_matched(self):
        return self.grid.all_matched()
