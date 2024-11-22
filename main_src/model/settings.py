import pygame
import os

# Screen dimensions
STATS_AREA_HEIGHT = 65  # Height of the stats area
SCORE_AREA_HEIGHT = 50 # Height of the high scores area
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
SCREEN_HEIGHT = STATS_AREA_HEIGHT + GRID_AREA_HEIGHT + SCORE_AREA_HEIGHT  # Total screen height
# to fit stats area and grid

# Colors
BACKGROUND_COLOR = (255, 255, 255)
PADDING_COLOR = (230, 230, 230)  # Light gray background for the padding area
BORDER_COLOR = (0, 0, 0)
_hidden_tile_color = (0, 0, 0)

# Game Limits (adjustable for difficulty)
FLIP_DURATION = 0.5  # Seconds tiles stay revealed
TIME_LIMIT = 180  # Seconds, 0 for no limit
MOVE_LIMIT = 50  # Moves, 0 for no limit


def get_font():
    if not pygame.font.get_init():
        pygame.font.init()
    return pygame.font.Font(None, 36)


def get_hidden_tile_color():
    return _hidden_tile_color


# Load Images
def get_theme(theme):
    """
    Configures the game theme by setting the hidden tile color and loading the appropriate image.
    :param theme: The selected theme ("pikachu" or "squirtle").
    """
    global _hidden_tile_color

    main_src_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))

    if theme == "pikachu":
        image_filename = "pikachu.png"
        _hidden_tile_color = (251, 202, 60)  # Pikachu yellow
    elif theme == "squirtle":
        image_filename = "squirtle.png"
        _hidden_tile_color = (103, 222, 229)  # Squirtle blue
    else:
        raise ValueError(f"Unknown theme: {theme}")

    image_path = os.path.join(main_src_path, 'assets', image_filename)
    print(f"Loading image from: {image_path}")

    try:
        # Load the image
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return None  # Return a fallback value

    # Check if the image loaded successfully
    if not isinstance(image, pygame.Surface):
        print("Error: Loaded image is not a valid pygame.Surface object")
        return None

    # Scale the image
    scaled_image = pygame.transform.scale(image,
                                          (TILE_SIZE // 2, TILE_SIZE // 2))

    return scaled_image
