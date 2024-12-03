from model.scorekeeper import ScoreKeeper


class StateController:
    """
    The StateController class manages the instantiation of and transitions
    between other controller instances. It also retrieves, maintains, and passes along
    attributes required for initializing states.
    """
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.score_keeper = ScoreKeeper()  # Shared ScoreKeeper instance

    def run(self, screen):
        while self.current_state:
            next_action = self.current_state.run(screen)

            if next_action == "QUIT":
                break
            elif next_action == "MENU":
                from controller.menu_state import MenuState
                self.current_state = MenuState(self)
            elif next_action == "GAME":
                from controller.game_state import GameState
                self.current_state = GameState(self, theme=self.current_state.selected_theme)
            elif next_action == "LEADERBOARD":
                from controller.leaderboard_state import LeaderboardState
                self.current_state = LeaderboardState(
                    self,
                    result=self.current_state.result,
                    time_elapsed=self.current_state.time_elapsed,
                    moves=self.current_state.moves,
                )