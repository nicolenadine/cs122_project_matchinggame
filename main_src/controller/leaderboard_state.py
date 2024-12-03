import pygame
from controller.base_state import BaseState
from model.settings import BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT


class LeaderboardState(BaseState):
    """
    This controller class inherits from BaseState Class and must implement
    run method. The LeaderboardState class controls the screen and behavior
    components for the leaderboard window that displays current game score
    and top scores.
    """
    def __init__(self, controller, result, time_elapsed, moves):
        super().__init__(controller)
        self.result = result
        self.time_elapsed = time_elapsed
        self.moves = moves
        self.score_keeper = self.controller.score_keeper
        self.score_keeper.load_scores()  # Ensure leaderboards are refreshed

    def handle_events(self):
        """
        Handle user input events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event detected")
                return "QUIT"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Returning to menu")
                    return "MENU"

        return "LEADERBOARD"

    def update(self):
        """
        Update method for LeaderboardState.
        Since there's no ongoing logic, return the current state.
        """
        return "LEADERBOARD"

    def render(self, screen):
        """
        Render the leaderboard screen.
        """
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.Font(None, 36)

        # Display current game stats
        current_game = self.score_keeper.get_current_game_stats()
        if current_game:
            current_text = f"Time: {current_game['time']:.2f}s, Moves: {current_game['moves']}"
            current_surface = font.render(current_text, True, (0, 0, 0))
            screen.blit(current_surface, (SCREEN_WIDTH // 2 - 150, 50))

        # Display top 5 best times
        top_times = self.score_keeper.get_top_times()
        times_title = font.render("Top 5 Best Times", True, (0, 0, 0))
        screen.blit(times_title, (SCREEN_WIDTH // 2 - 80, 100))
        for i, attempt in enumerate(top_times):
            time_text = f"{i + 1}. Time: {attempt['time']:.2f}s, Moves: {attempt['moves']}"
            time_surface = font.render(time_text, True, (0, 0, 0))
            screen.blit(time_surface, (SCREEN_WIDTH // 2 - 200, 140 + i * 30))

        # Display top 5 least moves
        top_moves = self.score_keeper.get_top_moves()
        moves_title = font.render("Top 5 Least Moves", True, (0, 0, 0))
        screen.blit(moves_title, (SCREEN_WIDTH // 2 - 80, 300))
        for i, attempt in enumerate(top_moves):
            move_text = f"{i + 1}. Moves: {attempt['moves']}, Time: {attempt['time']:.2f}s"
            move_surface = font.render(move_text, True, (0, 0, 0))
            screen.blit(move_surface, (SCREEN_WIDTH // 2 - 200, 340 + i * 30))

        # Instructions to return to menu
        return_to_menu_text = "Press ENTER to return to the menu."
        return_to_menu_surface = font.render(return_to_menu_text, True,
                                             (0, 0, 0))
        screen.blit(return_to_menu_surface,
                    (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 50))

        pygame.display.flip()

    def run(self, screen):
        """
        Main loop for the leaderboard state.
        :param screen
        """
        while True:
            next_action = self.handle_events()
            if next_action != "LEADERBOARD":
                return next_action

            next_action = self.update()
            if next_action != "LEADERBOARD":
                return next_action

            self.render(screen)
