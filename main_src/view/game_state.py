import pygame
import time
from view.ui import display_timers, \
    display_end_message  # Import utility functions if needed
from controller.grid_controller import GridController
from model.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, \
    PADDING_WIDTH, LEFT_MARGIN, TIME_LIMIT, MOVE_LIMIT, get_image


class GameState:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.game_running = True
        self.grid_controller = GridController(image=get_image())  # Initialize
        # game elements
        self.start_time = time.time()
        self.result = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.result and event.pos[0] > (
                    PADDING_WIDTH + LEFT_MARGIN):
                    adjusted_pos = (
                        event.pos[0] - PADDING_WIDTH - LEFT_MARGIN,
                        event.pos[1])
                    self.grid_controller.handle_click(adjusted_pos)

    def update(self):
        time_elapsed = time.time() - self.start_time
        self.time_remaining = max(TIME_LIMIT - time_elapsed,
                                  0) if TIME_LIMIT else None
        self.moves_remaining = max(MOVE_LIMIT - self.grid_controller.grid.moves,
                                   0) if MOVE_LIMIT else None

        # Check for win or loss
        if self.grid_controller.all_matched():
            self.result = "win"
            self.game_running = False  # Stop the game loop
        elif TIME_LIMIT and self.time_remaining <= 0:
            self.result = "lose"
            self.game_running = False  # Stop the game loop
        elif MOVE_LIMIT and self.moves_remaining <= 0:
            self.result = "lose"
            self.game_running = False  # Stop the game loop

    def render(self, screen):
        screen.fill(BACKGROUND_COLOR)
        self.grid_controller.draw(screen)
        display_timers(screen, self.time_remaining, self.moves_remaining)

        # If game over, display result
        if self.result:
            display_end_message(screen, self.result)

        pygame.display.flip()
