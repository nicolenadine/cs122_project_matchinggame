import pygame
import time
from view.ui import display_timers, display_end_message
from controller.grid_controller import GridController
from model.settings import (BACKGROUND_COLOR, TIME_LIMIT, MOVE_LIMIT, get_image, STATS_AREA_HEIGHT)


class GameState:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.game_running = True
        self.grid_controller = GridController(image=get_image())  # Initialize grid controller
        self.start_time = time.time()
        self.time_remaining = TIME_LIMIT
        self.moves = 0
        self.moves_remaining = MOVE_LIMIT
        self.result = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.result:
                    adjusted_pos = (
                        event.pos[0],  # No horizontal padding
                        event.pos[1] - STATS_AREA_HEIGHT  # Adjust for stats area height
                    )
                    if adjusted_pos[1] >= 0:  # Ensure click is below the stats area
                        self.grid_controller.handle_click(adjusted_pos)
                        self.grid_controller.process_tile_selection()  # Handle tile matching logic

    def update(self):
        time_elapsed = time.time() - self.start_time
        self.time_remaining = max(TIME_LIMIT - time_elapsed, 0) if TIME_LIMIT else None
        self.moves_remaining = max(MOVE_LIMIT - self.moves, 0) if MOVE_LIMIT else None

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
        self.grid_controller.draw(screen)  # Draw the grid
        display_timers(screen, self.time_remaining, self.moves_remaining)  # Display stats

        # If game over, display the result
        if self.result:
            display_end_message(screen, self.result)

        pygame.display.flip()
