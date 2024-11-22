import json
import os


class ScoreKeeper:
    def __init__(self, file_path="score_data.json"):
        self.file_path = file_path
        self.best_time = None  # Best time in seconds
        self.total_moves = None  # Best total moves
        self.load_scores()

    def load_scores(self):
        """Load scores from a JSON file."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    self.best_time = data.get("best_time", None)
                    self.total_moves = data.get("total_moves", None)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading scores: {e}")
                self.best_time = None
                self.total_moves = None
        else:
            self.best_time = None
            self.total_moves = None

    def save_scores(self):
        """Save scores to a JSON file."""
        try:
            with open(self.file_path, "w") as file:
                data = {
                    "best_time": self.best_time,
                    "total_moves": self.total_moves,
                }
                json.dump(data, file)
        except IOError as e:
            print(f"Error saving scores: {e}")

    def update_scores(self, time_elapsed, moves):
        """Update scores if the current game beats the records."""
        if self.best_time is None or time_elapsed < self.best_time:
            self.best_time = time_elapsed
        if self.total_moves is None or moves < self.total_moves:
            self.total_moves = moves
        self.save_scores()


