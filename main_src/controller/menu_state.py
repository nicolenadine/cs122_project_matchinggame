import pygame
from controller.base_state import BaseState
from model.settings import load_themes
from model.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class MenuState(BaseState):
    """
    This controller class inherits from BaseState Class and must implement
    run method. The MenuState class controls the menu screen which is
    displayed to the user before starting a new game. The main menu is where
    a user selects a theme.
    """
    def __init__(self, controller):
        super().__init__(controller)
        self.selected_theme = None  # No theme selected by default
        self.themes = load_themes()  # Load available themes dynamically
        self.theme_buttons = {}  # Stores theme button Rects
        self.start_button_rect = pygame.Rect(200, 500, 200, 50)  # Start button

        self.radio_button_size = 20
        self.spacing = 50
        self._generate_theme_buttons()

    def _generate_theme_buttons(self):
        """
        Generate radio button positions dynamically for each theme.
        """
        y_start = 340  # Starting y-coordinate for the radio buttons
        x_position = 40  # x-coordinate for the radio buttons

        for i, theme_name in enumerate(self.themes.keys()):
            self.theme_buttons[theme_name] = pygame.Rect(
                x_position, y_start + i * self.spacing, self.radio_button_size, self.radio_button_size
            )
            if self.selected_theme is None:
                # Default to the first theme in the CSV
                self.selected_theme = theme_name

    def handle_events(self):
        """
        Handle user input events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event detected")
                return "QUIT"  # Exit the application
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse clicked at: {event.pos}")
                if self.start_button_rect.collidepoint(event.pos):
                    print("Start button clicked!")
                    return "GAME"  # Transition to GameState
                # Check if a theme button was clicked
                for theme_name, button_rect in self.theme_buttons.items():
                    if button_rect.collidepoint(event.pos):
                        print(f"Theme button clicked: {theme_name}")
                        self.selected_theme = theme_name

        return "MENU"  # Stay in the current state

    def render(self, screen):
        """
        Render the menu screen.
        """
        screen.fill((240, 240, 240))  # Background color

        font = pygame.font.Font(None, 36)

        # Render instructions
        instructions = [
            "Match all pairs to win.",
            "Click on tiles to reveal them.",
            "Match pairs of tiles within time and move limits.",
        ]
        for i, instruction in enumerate(instructions):
            text_surface = font.render(instruction, True, (0, 0, 0))
            screen.blit(text_surface, (20, 20 + i * 50))

        # Render theme selection
        theme_font = pygame.font.Font(None, 28)
        theme_label = theme_font.render("Select Theme:", True, (0, 0, 0))
        screen.blit(theme_label, (20, 300))

        for theme_name, button_rect in self.theme_buttons.items():
            # Draw radio button
            pygame.draw.circle(screen, (0, 0, 0), button_rect.center, self.radio_button_size // 2, 2)
            if self.selected_theme == theme_name:
                # Draw selected theme indicator
                pygame.draw.circle(screen, (0, 200, 0), button_rect.center, self.radio_button_size // 2 - 4)

            # Draw theme label
            label_surface = theme_font.render(theme_name.capitalize(), True, (0, 0, 0))
            screen.blit(label_surface, (button_rect.right + 10, button_rect.y - 5))

        # Render the start button
        pygame.draw.rect(screen, (0, 200, 0), self.start_button_rect)  # Green start button
        start_text = font.render("Start Game", True, (255, 255, 255))
        screen.blit(start_text, (self.start_button_rect.x + 35, self.start_button_rect.y + 10))

        pygame.display.flip()

    def run(self, screen):
        """
        Main loop for the menu state.
        :param screen
        """
        while True:
            # Handle events and check for state transition
            next_action = self.handle_events()
            if next_action != "MENU":
                return next_action

            # Render the menu
            self.render(screen)
