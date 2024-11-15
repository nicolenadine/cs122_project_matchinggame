import pygame
from controller.state_controller import StateController
from controller.menu_state import MenuState
from model.settings import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    # FONT = get_font()

    # Show the instructions screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Memory Match Game")

    # Initialize the state controller with the initial state (menu)
    initial_state = MenuState(None)
    state_controller = StateController(initial_state)
    initial_state.game_controller = state_controller  # Link state back to controller

    state_controller.run(screen)
    pygame.quit()


if __name__ == "__main__":
    main()
