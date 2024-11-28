import pygame
from controller.state_controller import StateController
from controller.menu_state import MenuState
from model.settings import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()

    # Initialize the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Memory Match Game")

    # Create the StateController with MenuState as the initial state
    state_controller = StateController(MenuState(None))
    state_controller.run(screen)

    pygame.quit()


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
