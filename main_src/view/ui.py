import pygame
from model.settings import get_font, TIME_LIMIT, MOVE_LIMIT, PADDING_COLOR, \
    PADDING_WIDTH, SCREEN_HEIGHT


def display_timers(screen, time_remaining, moves_remaining):
    """ Display the countdown timers in the padding area. """
    # Draw background for the padding area
    pygame.draw.rect(screen, PADDING_COLOR,
                     (0, 0, PADDING_WIDTH, SCREEN_HEIGHT))

    # Display the time limit countdown
    time_text = f"Time Left: {int(time_remaining)}s" if time_remaining > 0 else "Time's Up!"
    time_surface = get_font().render(time_text, True, (0, 0, 0))
    screen.blit(time_surface, (20, 100))

    # Display the move limit countdown
    move_text = f"Moves Left: {moves_remaining}" if moves_remaining > 0 else "No Moves Left!"
    move_surface = get_font().render(move_text, True, (0, 0, 0))
    screen.blit(move_surface, (20, 150))


def display_message(screen, message, color, position):
    text_surface = get_font().render(message, True, color)
    screen.blit(text_surface, position)


def display_end_message(screen, result):
    if result == "win":
        message = "You Win!"
        color = (0, 255, 0)
    else:
        message = "Game Over!"
        color = (255, 0, 0)
    display_message(screen, message, color, (200, 300))


def show_instructions():
    # Create an instructions window with game rules
    pygame.display.set_caption("Game Instructions")
    instruction_screen = pygame.display.set_mode((600, 600))
    instruction_screen.fill((240, 240, 240))

    # Display instructions text
    messages = [
        "Match all pairs to win.",
        "Click on tiles to reveal them.",
        "Match pairs of tiles within time and move limits.",
        f"Time Limit: {TIME_LIMIT} seconds" if TIME_LIMIT else "No Time Limit",
        f"Move Limit: {MOVE_LIMIT} moves" if MOVE_LIMIT else "No Move Limit",
    ]

    for i, message in enumerate(messages):
        display_message(instruction_screen, message, (0, 0, 0),
                        (20, 20 + i * 50))

    # Create the start button
    button_color = (0, 200, 0)  # Green color for the button
    button_rect = pygame.Rect(200, 500, 200, 50)  # Button position and size
    pygame.draw.rect(instruction_screen, button_color, button_rect)
    display_message(instruction_screen, "Start Game", (255, 255, 255),
                    (button_rect.x + 35, button_rect.y + 10))

    pygame.display.flip()

    # Wait for the user to either close the window or click the start button
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                exit()  # Ensure the program exits completely if the user closes this window
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False  # Exit the loop to transition to the game

#   pygame.display.quit()