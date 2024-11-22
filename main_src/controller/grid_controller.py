import pygame
from model.settings import FLIP_DURATION, GRID_SIZE, TILE_SIZE, BORDER_WIDTH, \
    STATS_AREA_HEIGHT
from view.grid import Grid


class GridController:
    def __init__(self, image):
        self.image = image if image is not None else self.create_placeholder_image()
        self.grid = Grid(self.image)
        self.waiting_for_match = False  # Flag to track if we're waiting for a second tile
        self.move_callback = None

    def create_placeholder_image(self):
        placeholder_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        placeholder_image.fill((255, 255, 255))
        return placeholder_image

    def handle_click(self, pos):
        # Adjust click position to account for border and stats area
        adjusted_x = pos[0] // (TILE_SIZE + 2 * BORDER_WIDTH)
        adjusted_y = (pos[1] - STATS_AREA_HEIGHT) // (
                TILE_SIZE + 2 * BORDER_WIDTH)

        # Ensure click is within grid bounds
        if 0 <= adjusted_y < GRID_SIZE and 0 <= adjusted_x < GRID_SIZE:
            tile = self.grid.tiles[adjusted_y][adjusted_x]
            if not tile.matched and not tile.flipped:
                tile.flipped = True
                self.grid.revealed_tiles.append(tile)

                # Check for match only if two new tiles have been selected
                if len(self.grid.revealed_tiles) == 2:
                    self.process_tile_selection()

    def process_tile_selection(self):
        tile1, tile2 = self.grid.revealed_tiles

        # Notify that a move has been made
        self.move_callback()

        # If tiles are a match, mark them as matched
        if tile1.tile_type == tile2.tile_type:
            tile1.matched = True
            tile2.matched = True
            self.grid.revealed_tiles.clear()
        else:
            # Set a flag to delay flipping back over non-matching tiles
            self.waiting_for_match = True
            pygame.time.set_timer(pygame.USEREVENT, int(FLIP_DURATION * 1000))

    def handle_timer_event(self):
        # Flip the tiles back over if they didn't match after the delay
        if self.waiting_for_match and len(self.grid.revealed_tiles) == 2:
            tile1, tile2 = self.grid.revealed_tiles
            tile1.flipped = False
            tile2.flipped = False
            self.grid.revealed_tiles.clear()
            self.waiting_for_match = False
            pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer

    def draw(self, screen):
        self.grid.draw(screen)

    def all_matched(self):
        return self.grid.all_matched()
