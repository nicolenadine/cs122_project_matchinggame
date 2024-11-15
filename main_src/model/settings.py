import pygame
import os

# Screen and Grid Settings
PADDING_WIDTH = 200  # Width of the left padding for timers
LEFT_MARGIN = 20  # Margin between left padding and game grid
SCREEN_WIDTH, SCREEN_HEIGHT = PADDING_WIDTH + LEFT_MARGIN + 800, 800  # Adjusted width
GRID_SIZE = 6  # Increased grid size
BORDER_WIDTH = 2  # Thickness of the border around each tile
TILE_SIZE = (SCREEN_WIDTH - PADDING_WIDTH - LEFT_MARGIN) // GRID_SIZE - 2 * BORDER_WIDTH  # Adjust tile size for the border

# Colors
BACKGROUND_COLOR = (255, 255, 255)
PADDING_COLOR = (230, 230, 230)  # Light gray background for the padding area
HIDDEN_TILE_COLOR = (255, 0, 0)
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
