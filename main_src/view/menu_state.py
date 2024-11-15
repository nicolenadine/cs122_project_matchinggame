import pygame
from view.game_state import GameState  # Import GameState to transition


class MenuState:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.game_running = True

        # Set up instruction screen elements
        self.button_rect = pygame.Rect(200, 500, 200, 50)  # Button position and size

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    # Transition to the game state when the start button is clicked
                    new_state = GameState(self.game_controller)
                    self.game_controller.change_state(new_state)

    def update(self):
        # Any menu update logic goes here (if needed)
        pass

    def render(self, screen):
        # Display instructions
        screen.fill((240, 240, 240))  # Background color for instructions

        messages = [
            "Match all pairs to win.",
            "Click on tiles to reveal them.",
            "Match pairs of tiles within time and move limits.",
            f"Time Limit: {self.game_controller.TIME_LIMIT} seconds" if hasattr(self.game_controller, 'TIME_LIMIT') and self.game_controller.TIME_LIMIT else "No Time Limit",
            f"Move Limit: {self.game_controller.MOVE_LIMIT} moves" if hasattr(self.game_controller, 'MOVE_LIMIT') and self.game_controller.MOVE_LIMIT else "No Move Limit",
        ]

        font = pygame.font.Font(None, 36)  # Example font, replace with your font settings if needed
        for i, message in enumerate(messages):
            text_surface = font.render(message, True, (0, 0, 0))
            screen.blit(text_surface, (20, 20 + i * 50))

        # Draw the start button
        button_color = (0, 200, 0)  # Green color for the button
        pygame.draw.rect(screen, button_color, self.button_rect)
        button_text = font.render("Start Game", True, (255, 255, 255))
        screen.blit(button_text, (self.button_rect.x + 35, self.button_rect.y + 10))

        pygame.display.flip()
