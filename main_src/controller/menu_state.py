import pygame
from controller.game_state import GameState  # Import GameState to transition


class MenuState:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.button_rect = pygame.Rect(200, 500, 200,
                                       50)  # Start button
        self.selected_theme = "pikachu"  # Default theme
        self.pikachu_button_rect = None
        self.squirtle_button_rect = None
        self.game_running = True

        # Set up instruction screen elements
        self.button_rect = pygame.Rect(200, 500, 200, 50)  # Button position and size

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    # Start game with selected theme
                    self.game_controller.change_state(
                        GameState(self.game_controller,
                                  theme=self.selected_theme))
                elif self.pikachu_button_rect.collidepoint(event.pos):
                    self.selected_theme = "pikachu"
                elif self.squirtle_button_rect.collidepoint(event.pos):
                    self.selected_theme = "squirtle"

    def update(self):
        pass

    def render(self, screen):
        # Display instructions
        screen.fill((240, 240, 240))  # Bg color for instructions

        # Render instructions
        messages = [
            "Match all pairs to win.",
            "Click on tiles to reveal them.",
            "Match pairs of tiles within time and move limits.",
            f"Time Limit: {self.game_controller.TIME_LIMIT} seconds" if hasattr(
                self.game_controller,
                'TIME_LIMIT') and self.game_controller.TIME_LIMIT else "No Time Limit",
            f"Move Limit: {self.game_controller.MOVE_LIMIT} moves" if hasattr(
                self.game_controller,
                'MOVE_LIMIT') and self.game_controller.MOVE_LIMIT else "No Move Limit",
        ]

        font = pygame.font.Font(None, 36)
        for i, message in enumerate(messages):
            text_surface = font.render(message, True, (0, 0, 0))
            screen.blit(text_surface, (20, 20 + i * 50))

        # Render theme selection
        theme_font = pygame.font.Font(None, 28)
        theme_message = theme_font.render("Select Theme:", True, (0, 0, 0))
        screen.blit(theme_message, (20, 300))  # Position for theme message

        # Draw radio buttons for Pikachu and Squirtle
        radio_button_size = 20
        spacing = 50
        self.pikachu_button_rect = pygame.Rect(40, 340, radio_button_size,
                                               radio_button_size)
        self.squirtle_button_rect = pygame.Rect(40, 340 + spacing,
                                                radio_button_size,
                                                radio_button_size)

        pygame.draw.circle(screen, (0, 0, 0), self.pikachu_button_rect.center,
                           radio_button_size // 2, 2)
        pygame.draw.circle(screen, (0, 0, 0), self.squirtle_button_rect.center,
                           radio_button_size // 2, 2)

        # Fill the selected theme button
        if self.selected_theme == "pikachu":
            pygame.draw.circle(screen, (0, 200, 0),
                               self.pikachu_button_rect.center,
                               radio_button_size // 2 - 4)
        elif self.selected_theme == "squirtle":
            pygame.draw.circle(screen, (0, 200, 0),
                               self.squirtle_button_rect.center,
                               radio_button_size // 2 - 4)

        # Add labels for the radio buttons
        pikachu_label = theme_font.render("Pikachu", True, (0, 0, 0))
        squirtle_label = theme_font.render("Squirtle", True, (0, 0, 0))
        screen.blit(pikachu_label, (
        self.pikachu_button_rect.right + 10, self.pikachu_button_rect.y - 5))
        screen.blit(squirtle_label, (
        self.squirtle_button_rect.right + 10, self.squirtle_button_rect.y - 5))

        # Draw the start button
        button_color = (0, 200, 0)  # Green color for the button
        pygame.draw.rect(screen, button_color, self.button_rect)
        button_text = font.render("Start Game", True, (255, 255, 255))
        screen.blit(button_text,
                    (self.button_rect.x + 35, self.button_rect.y + 10))

        pygame.display.flip()
