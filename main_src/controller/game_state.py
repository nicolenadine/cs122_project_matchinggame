import pygame
import time
from controller.base_state import BaseState
from view.ui import display_timers
from controller.grid_controller import GridController
from model.settings import BACKGROUND_COLOR, TIME_LIMIT, MOVE_LIMIT, get_theme


class GameState(BaseState):
    def __init__(self, controller, theme):
        super().__init__(controller)
        self.theme = theme
        self.start_time = time.time()
        self.time_remaining = TIME_LIMIT
        self.moves = 0
        self.moves_remaining = MOVE_LIMIT
        self.result = None

        # Initialize the scorekeeper and grid controller
        self.score_keeper = self.controller.score_keeper
        self.grid_controller = GridController(image=get_theme(theme))
        self.grid_controller.move_callback = self.increment_moves

    def handle_events(self):
        """
        Handle user input events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event detected")
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.result:  # Only process clicks while the game is running
                    adjusted_pos = (
                        event.pos[0],
                        event.pos[1] - 100  # Adjust for stats area height
                    )
                    if adjusted_pos[1] >= 0:  # Ensure click is below the stats area
                        self.grid_controller.handle_click(adjusted_pos)
            elif event.type == pygame.USEREVENT:
                self.grid_controller.handle_timer_event()

        return "GAME"  # Stay in the current state

    def update(self):
        """
        Update game logic and check for win/loss conditions.
        """
        time_elapsed = time.time() - self.start_time
        self.time_remaining = max(TIME_LIMIT - time_elapsed, 0) if TIME_LIMIT else None

        if self.grid_controller.all_matched():
            self.result = "win"
            self.time_elapsed = time_elapsed
            self.score_keeper.set_current_game_score(self.time_elapsed, self.moves)
            return "LEADERBOARD"
        elif TIME_LIMIT and self.time_remaining <= 0:
            self.result = "lose"
            self.time_elapsed = time_elapsed
            self.score_keeper.set_current_game_score(self.time_elapsed, self.moves)
            return "LEADERBOARD"
        elif MOVE_LIMIT and self.moves_remaining <= 0:
            self.result = "lose"
            self.time_elapsed = time_elapsed
            self.score_keeper.set_current_game_score(self.time_elapsed, self.moves)
            return "LEADERBOARD"

        return "GAME"

    def render(self, screen):
        """
        Render the game screen.
        """
        screen.fill(BACKGROUND_COLOR)

        # Draw the grid and stats
        self.grid_controller.draw(screen)
        display_timers(screen, self.time_remaining, self.moves_remaining, self.moves)

        pygame.display.flip()

    def increment_moves(self):
        """
        Increment the number of moves made by the player.
        """
        self.moves += 1
        self.moves_remaining = max(MOVE_LIMIT - self.moves, 0)

    def run(self, screen):
        """
        Main loop for the game state.
        """
        while True:
            next_action = self.handle_events()
            if next_action != "GAME":
                return next_action

            next_action = self.update()
            if next_action != "GAME":
                return next_action

            self.render(screen)
