import pygame
import os

# Screen dimensions
STATS_AREA_HEIGHT = 65  # Height of the stats area
TILE_SIZE = 150  # Size of each tile
GRID_SIZE = 4  # 4x4 grid
BORDER_WIDTH = 10  # Border around each tile
WHITESPACE = 10  # Additional whitespace between tiles

# Calculate total dimensions of each tile (including border and whitespace)
TILE_TOTAL_SIZE = TILE_SIZE + 2 * BORDER_WIDTH + WHITESPACE

# Calculate the total dimensions of the grid
GRID_AREA_WIDTH = GRID_SIZE * TILE_TOTAL_SIZE - WHITESPACE  # Subtract whitespace at the end
GRID_AREA_HEIGHT = GRID_SIZE * TILE_TOTAL_SIZE - WHITESPACE  # Subtract whitespace at the end


# Screen size calculation
SCREEN_WIDTH = GRID_AREA_WIDTH  # Set the screen width to fit the grid area
SCREEN_HEIGHT = STATS_AREA_HEIGHT + GRID_AREA_HEIGHT  # Total screen height to fit stats area and grid

# Colors
BACKGROUND_COLOR = (255, 255, 255)
PADDING_COLOR = (230, 230, 230)  # Light gray background for the padding area
HIDDEN_TILE_COLOR = (251, 202, 60)
BORDER_COLOR = (0, 0, 0)

# Game Limits (adjustable for difficulty)
FLIP_DURATION = 0.5  # Seconds tiles stay revealed
TIME_LIMIT = 180  # Seconds, 0 for no limit
MOVE_LIMIT = 160  # Moves, 0 for no limit


def get_font():
    if not pygame.font.get_init():
        pygame.font.init()
    return pygame.font.Font(None, 36)


# Load Images
def get_image():
    main_src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    image_path = os.path.join(main_src_path, 'assets', 'image.png')
    print(f"Loading image from: {image_path}")

    try:
        # Load the image
        image = pygame.image.load(image_path)
    except pygame.error as e:
        # image load failure
        print(f"Error loading image: {e}")
        return None  # Return None or a default/fallback surface

    # Check if the image loaded successfully
    if not isinstance(image, pygame.Surface):
        print("Error: Loaded image is not a valid pygame.Surface object")
        return None

    return pygame.transform.scale(image, (TILE_SIZE // 2, TILE_SIZE // 2))
