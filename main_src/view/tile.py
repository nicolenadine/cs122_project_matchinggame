import pygame
from model.settings import (TILE_SIZE, get_hidden_tile_color, BORDER_COLOR,
                            BORDER_WIDTH)


class Tile:
    """
    The Tile class renders tiles on the screen according to
    specified measurements. The tiles will have a tile_type, color, x and y location,
    as well as an image to be placed in the center of the hidden side. Tiles
    can be drawn in a hidden state or revealed state.
    """
    def __init__(self, tile_type, color, x, y, image):
        self.tile_type = tile_type
        self.color = color  # Set the unique color for the tile type
        self.x = x
        self.y = y
        self.matched = False
        self.flipped = False
        self.flipped_image = image

    def draw(self, screen):
        """
        Calls on methods to draw a tile in hidden or revealed state based on
        the status of the flipped and matched attributes
        :param screen:
        """
        if self.flipped or self.matched:
            self.draw_revealed(screen)
        else:
            self.draw_hidden(screen)

    def draw_hidden(self, screen):
        """
        Draws a tile in the hidden state where it contains the main theme
        color and a border.
        :param screen:
        """
        # Draw the hidden state with a border
        pygame.draw.rect(screen, get_hidden_tile_color(),
                         (self.x, self.y, TILE_SIZE, TILE_SIZE))

        # Draw the border around the tile
        pygame.draw.rect(screen, BORDER_COLOR,
                         (self.x, self.y, TILE_SIZE, TILE_SIZE), BORDER_WIDTH)

    def draw_revealed(self, screen):
        """
        Draws a tile in the revaled state where it displays the tile's unique color
        with the theme image centered in the tile.
        :param screen:
        """
        # Draw the revealed state with the background color
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, TILE_SIZE, TILE_SIZE))

        # Draw the border around the revealed tile
        pygame.draw.rect(screen, BORDER_COLOR,
                         (self.x, self.y, TILE_SIZE, TILE_SIZE), BORDER_WIDTH)

        # Center the image on the tile
        image_rect = self.flipped_image.get_rect(
            center=(self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2))
        screen.blit(self.flipped_image, image_rect)
