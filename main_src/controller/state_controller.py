class StateController:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def change_state(self, new_state):
        self.current_state = new_state

    def run(self, screen):
        running = True
        while running:
            # Handle events, update state, and render
            self.current_state.handle_events()
            self.current_state.update()
            self.current_state.render(screen)

            # Exit if the current state signals to stop
            if not self.current_state.game_running:
                running = False
