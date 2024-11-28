class BaseState:
    def __init__(self, controller):
        self.controller = controller

    def run(self, screen):
        """
        Handle events, updates, and rendering for this state.
        Should return the next state or None to exit.
        """
        raise NotImplementedError("Subclasses must implement the run method")
