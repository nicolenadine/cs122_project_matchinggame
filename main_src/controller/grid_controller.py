import pygame
from model.settings import FLIP_DURATION, GRID_SIZE, TILE_SIZE, BORDER_WIDTH, \
    STATS_AREA_HEIGHT, WHITESPACE, TILE_TOTAL_SIZE
from view.grid import Grid


class GridController:
    """
    A class to manage the game board including the grid class and tile class
    instances.
    """
    def __init__(self, image):
        self.image = image if image is not None else self.create_placeholder_image()
        self.grid = Grid(self.image)
        self.waiting_for_match = False  # Flag to track if we're waiting for a second tile
        self.move_callback = None
        self.flip_timer_active = False  # Track if a flip timer is active
        self.click_locked = False # lock to prevent rapid clicking
                                  # Unlock after match or timer event


    def create_placeholder_image(self):
        """
        In the event there is not a valid image passed to constructor.
        Generate a placeholder colored square to substitute
        :return: surface object
        """
        placeholder_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        placeholder_image.fill((255, 255, 255))
        return placeholder_image

    def handle_click(self, pos):
        """
        Processes user clicks in the grid area and applies adjustments to
        determine which tiles to flip and when to check for a match
        :param pos: position of user click
        """
        if self.click_locked:
            print("Click ignored")  # Debug logging
            return

        adjusted_x = (pos[0] - WHITESPACE) // TILE_TOTAL_SIZE
        adjusted_y = ((pos[1] - WHITESPACE + STATS_AREA_HEIGHT) //
                      TILE_TOTAL_SIZE)

        # Ensure click is within grid bounds
        if 0 <= adjusted_y < GRID_SIZE and 0 <= adjusted_x < GRID_SIZE:
            tile = self.grid.tiles[adjusted_y][adjusted_x]
            if not tile.matched and not tile.flipped and not self.waiting_for_match:
                print(f"Tile clicked at ({adjusted_x}, {adjusted_y})")  # Debug logging
                tile.flipped = True
                self.grid.revealed_tiles.append(tile)

                # Check for match only if two new tiles have been selected
                if len(self.grid.revealed_tiles) == 2:
                    self.process_tile_selection()

    def process_tile_selection(self):
        """
        Check if two revealed tiles are a match. If yes, remain flipped. If
        no, return to hidden state
        """
        tile1, tile2 = self.grid.revealed_tiles

        # Notify that a move has been made
        if callable(self.move_callback):
            self.move_callback()
        else:
            print("Warning: callback error")

        # If tiles are a match, mark them as matched
        if tile1.tile_type == tile2.tile_type:
            tile1.matched = True
            tile2.matched = True
            self.grid.revealed_tiles.clear()
            self.click_locked = False  # Unlock after match
        else:
            # Set a flag to delay flipping back over non-matching tiles
            self.waiting_for_match = True
            if not self.flip_timer_active:  # Prevent duplicate timers
                self.flip_timer_active = True
                pygame.time.set_timer(pygame.USEREVENT, int(FLIP_DURATION * 1000))

    def handle_timer_event(self):
        """
        After time runs out flip unmatched tiles back to hidden
        """
        # Flip the tiles back over if they didn't match after the delay
        if self.waiting_for_match and len(self.grid.revealed_tiles) == 2:
            tile1, tile2 = self.grid.revealed_tiles
            tile1.flipped = False
            tile2.flipped = False
            self.grid.revealed_tiles.clear()
            self.waiting_for_match = False
            self.flip_timer_active = False
            self.click_locked = False  # Unlock after mismatch is resolved
            pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer

    def draw(self, screen):
        """
        draw the grid of tiles on screen
        :param screen:
        """
        self.grid.draw(screen)

    def all_matched(self):
        """
        Calls Grid class all_matched() to check if all tiles have been matched.
        :return: Boolean
        """
        return self.grid.all_matched()
