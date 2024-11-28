import pygame
import os
import csv

# Screen dimensions
STATS_AREA_HEIGHT = 65
TILE_SIZE = 150
GRID_SIZE = 4
BORDER_WIDTH = 10
WHITESPACE = 10

# Calculate total dimensions
TILE_TOTAL_SIZE = TILE_SIZE + 2 * BORDER_WIDTH + WHITESPACE
GRID_AREA_WIDTH = GRID_SIZE * TILE_TOTAL_SIZE - WHITESPACE
GRID_AREA_HEIGHT = GRID_SIZE * TILE_TOTAL_SIZE - WHITESPACE
SCREEN_WIDTH = GRID_AREA_WIDTH
SCREEN_HEIGHT = (STATS_AREA_HEIGHT + GRID_AREA_HEIGHT)

# Colors
BACKGROUND_COLOR = (255, 255, 255)
PADDING_COLOR = (230, 230, 230)
BORDER_COLOR = (0, 0, 0)
_hidden_tile_color = (0, 0, 0)

# Game Limits
FLIP_DURATION = 1.5
TIME_LIMIT = 180
MOVE_LIMIT = 50

# Path to themes.csv
THEMES_CSV_PATH = os.path.join(os.path.dirname(__file__), "themes.csv")


def get_font():
    if not pygame.font.get_init():
        pygame.font.init()
    return pygame.font.Font(None, 36)


def get_hidden_tile_color():
    return _hidden_tile_color


def load_themes():
    """
    Loads theme data from the themes.csv file.
    :return: A dictionary of themes with their attributes.
    """
    themes = {}
    try:
        with open(THEMES_CSV_PATH, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                themes[row['name']] = {
                    'image_file_name': row['image_file_name'],
                    'primary_color': tuple(map(int, row['primary_color'].split('-'))),
                    'hidden_tile_color': tuple(map(int, row['hidden_tile_color'].split('-')))
                }
    except FileNotFoundError:
        print(f"Error: {THEMES_CSV_PATH} not found.")
    except Exception as e:
        print(f"Error reading {THEMES_CSV_PATH}: {e}")
    return themes


def get_theme(theme_name):
    """
    Retrieves theme information and configures the hidden tile color and image.
    :param theme_name: The name of the theme to retrieve.
    :return: A pygame.Surface of the theme's image.
    """
    global _hidden_tile_color

    themes = load_themes()
    if theme_name not in themes:
        raise ValueError(f"Unknown theme: {theme_name}")

    theme = themes[theme_name]
    _hidden_tile_color = theme['hidden_tile_color']

    # Load the image
    main_src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    image_path = os.path.join(main_src_path, 'assets', theme['image_file_name'])
    print(f"Loading image from: {image_path}")

    try:
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return None

    return pygame.transform.scale(image, (TILE_SIZE // 2, TILE_SIZE // 2))


def get_theme_color(theme_name):
    """
    Retrieves the primary and hidden tile colors for a given theme.
    :param theme_name: The name of the theme.
    :return: A tuple of (primary_color, hidden_tile_color).
    """
    themes = load_themes()
    if theme_name not in themes:
        raise ValueError(f"Unknown theme: {theme_name}")
    theme = themes[theme_name]
    return theme['primary_color'], theme['hidden_tile_color']
