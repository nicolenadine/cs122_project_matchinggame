import pygame
from model.settings import TILE_SIZE, HIDDEN_TILE_COLOR, BORDER_COLOR, \
    BORDER_WIDTH, get_image


class Tile:
    def __init__(self, tile_type, color, x, y, image):
        self.tile_type = tile_type
        self.color = color  # Set the unique color for the tile type
        self.x = x
        self.y = y
        self.matched = False
        self.flipped = False
        self.flipped_image = image

    def draw(self, screen):
        if self.flipped or self.matched:
            self.draw_revealed(screen)
        else:
            self.draw_hidden(screen)

    def draw_hidden(self, screen):
        pygame.draw.rect(screen, HIDDEN_TILE_COLOR,
                         (self.x, self.y, TILE_SIZE, TILE_SIZE))

        # Draw the border around the tile
        pygame.draw.rect(screen, BORDER_COLOR,
                         (self.x, self.y, TILE_SIZE, TILE_SIZE), BORDER_WIDTH)

    def draw_revealed(self, screen):
        # Draw the background color
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, TILE_SIZE, TILE_SIZE))

        # Draw the border around the revealed tile
        pygame.draw.rect(screen, BORDER_COLOR,
                         (self.x, self.y, TILE_SIZE, TILE_SIZE), BORDER_WIDTH)

        # Center the Pikachu image on the tile
        image_rect = self.flipped_image.get_rect(
            center=(self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2))
        screen.blit(self.flipped_image, image_rect)
