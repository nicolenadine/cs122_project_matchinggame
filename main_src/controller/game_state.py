import pygame
import time
from view.ui import display_timers, display_end_message
from controller.grid_controller import GridController
from model.settings import (BACKGROUND_COLOR, TIME_LIMIT, MOVE_LIMIT, get_theme,
                            STATS_AREA_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH)
from model.scorekeeper import ScoreKeeper

class GameState:
    def __init__(self, game_controller, theme):
        self.game_controller = game_controller
        self.game_running = True
        self.score_keeper = ScoreKeeper()
        self.start_time = time.time()
        self.time_remaining = TIME_LIMIT
        self.moves = 0
        self.moves_remaining = MOVE_LIMIT
        self.result = None

        # Initialize grid controller & call-back function for incrementing moves
        self.grid_controller = GridController(image=get_theme(theme))
        self.grid_controller.move_callback = self.increment_moves

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
            elif event.type == pygame.USEREVENT:
                # Handle the delayed flip-back event
                self.grid_controller.handle_timer_event()

    def update(self):
        time_elapsed = time.time() - self.start_time
        self.time_remaining = max(TIME_LIMIT - time_elapsed, 0) if TIME_LIMIT else None

        # Check for win or loss
        if self.grid_controller.all_matched():
            self.result = "win"
            self.game_running = False  # Stop the game loop
            self.score_keeper.update_scores(time_elapsed, self.moves)
        elif TIME_LIMIT and self.time_remaining <= 0:
            self.result = "lose"
            self.game_running = False  # Stop the game loop
            self.score_keeper.update_scores(time_elapsed, self.moves)
        elif MOVE_LIMIT and self.moves_remaining <= 0:
            self.result = "lose"
            self.game_running = False  # Stop the game loop
            self.score_keeper.update_scores(time_elapsed, self.moves)

    def render(self, screen):
        # Clear the screen and draw the background
        screen.fill(BACKGROUND_COLOR)

        # Draw the grid
        self.grid_controller.draw(screen)

        # Display the timers and stats at the top
        display_timers(screen, self.time_remaining, self.moves_remaining,
                       self.moves)

        # Display the scorekeeper stats at the bottom
        if self.score_keeper:  # Check if score_keeper is initialized
            font = pygame.font.Font(None, 36)
            best_time_text = (
                f"Best Time: {self.score_keeper.best_time:.2f} seconds"
                if self.score_keeper.best_time is not None else
                "Best Time: N/A"
            )
            total_moves_text = (
                f"Least Moves: {self.score_keeper.total_moves}"
                if self.score_keeper.total_moves is not None else
                "Least Moves: N/A"
            )

            # Render the text for best time
            best_time_surface = font.render(best_time_text, True, (0, 0, 0))
            screen.blit(best_time_surface, (20,
                                            SCREEN_HEIGHT - 50))  # Adjust Y-position for the bottom of the screen

            # Render the text for least moves
            total_moves_surface = font.render(total_moves_text, True, (0, 0, 0))
            screen.blit(total_moves_surface,
                        (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

        # If the game is over, display the result
        if self.result:
            display_end_message(screen, self.result)

        # Update the display
        pygame.display.flip()

    def increment_moves(self):
        self.moves += 1
        self.moves_remaining = max(MOVE_LIMIT - self.moves, 0)

