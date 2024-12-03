import json
import os


class ScoreKeeper:
    """
    The ScoreKeeper class manages the loading, updating, and saving of game
    scores. It works with a json file and only keeps the top scores in order to
    keep file size minimal.
    """
    def __init__(self, file_path="score_data.json"):
        self.file_path = file_path
        self.current_game = None  # Stats for the current game
        self.top_times = []  # Top 5 best times
        self.top_moves = []  # Top 5 least moves
        self.load_scores()

    def load_scores(self):
        """Load top scores from a JSON file."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    self.top_times = data.get("top_times", [])
                    self.top_moves = data.get("top_moves", [])
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading scores: {e}")
                self.top_times = []
                self.top_moves = []
        else:
            self.top_times = []
            self.top_moves = []

    def save_scores(self):
        """Save top scores to a JSON file."""
        try:
            with open(self.file_path, "w") as file:
                data = {
                    "top_times": self.top_times,
                    "top_moves": self.top_moves
                }
                json.dump(data, file)
        except IOError as e:
            print(f"Error saving scores: {e}")

    def set_current_game_score(self, time_elapsed, moves):
        """
        Set the stats for the current game and update leaderboards.
        """
        self.current_game = {"time": time_elapsed, "moves": moves}
        self.update_leaderboards()

    def update_leaderboards(self):
        """
        Update the top 5 leaderboards for time and moves based on the current game.
        """
        if not self.current_game:
            return

        # Update top times
        self.top_times.append(self.current_game)
        self.top_times = sorted(self.top_times, key=lambda x: x["time"])[:5]

        # Update top moves
        self.top_moves.append(self.current_game)
        self.top_moves = sorted(self.top_moves, key=lambda x: x["moves"])[:5]

        # Save updated leaderboards
        self.save_scores()

    def get_current_game_stats(self):
        """
        Return the stats for the current game.
        """
        return self.current_game

    def get_top_times(self):
        """
        Return the top 5 best times.
        """
        return self.top_times

    def get_top_moves(self):
        """
        Return the top 5 least moves.
        """
        return self.top_moves
