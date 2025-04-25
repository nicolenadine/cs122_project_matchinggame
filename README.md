# Pokémon Memory Match

A Pygame-based memory matching game featuring Pokémon themes.

## Overview

Pokémon Memory Match is a classic tile-matching memory game where players flip cards to find matching pairs. The game features customizable Pokémon themes, a timer, move counter, and leaderboard to track your best performances.

## Features

- **Multiple Pokémon Themes**: Choose from different Pokémon-themed card sets
- **Game Stats Tracking**: Monitor time remaining and moves used
- **Leaderboard System**: Tracks and displays your best times and fewest moves
- **Responsive UI**: Clean interface with game instructions and status updates
- **State Management**: Smooth transitions between menu, game, and leaderboard screens

## Game Rules

1. Click tiles to reveal what's underneath
2. Remember the locations of the tiles
3. Match all pairs before time runs out or move limit is reached
4. Your score is tracked based on time taken and number of moves used

## Technical Implementation

### Model-View-Controller Architecture

The game follows the MVC design pattern:

- **Model**: Manages game data and business logic
  - `settings.py`: Game constants and configuration
  - `scorekeeper.py`: Handles score tracking and persistence

- **View**: Responsible for rendering game elements
  - `tile.py`: Renders individual tiles in hidden or revealed states
  - `grid.py`: Manages the game board layout
  - `ui.py`: Handles UI elements and displays

- **Controller**: Handles game states and user interactions
  - `base_state.py`: Abstract class for all game states
  - `menu_state.py`: Main menu interface
  - `game_state.py`: Core gameplay logic
  - `leaderboard_state.py`: Score display and rankings
  - `grid_controller.py`: Manages tile interactions
  - `state_controller.py`: Orchestrates transitions between states

### State Management

The game uses a state machine to manage different screens:
- **Menu State**: Theme selection and game start
- **Game State**: Core gameplay with tile matching
- **Leaderboard State**: Display of current and best scores

## Installation & Setup

### Prerequisites
- Python 3.6+
- Pygame library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pokemon-memory-match.git
   cd pokemon-memory-match
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## How to Play

1. Launch the game using `python main.py`
2. Select a Pokémon theme from the menu
3. Click "Start Game" to begin
4. Click tiles to reveal them and find matching pairs
5. Match all pairs before time runs out or move limit is reached
6. View your performance on the leaderboard
7. Press ENTER to return to the main menu for another round

## Project Structure

```
pokemon-memory-match/
├── assets/                  # Game images and themes
├── controller/              # Game state controllers
│   ├── base_state.py        # Parent class for all states
│   ├── game_state.py        # Gameplay controller
│   ├── grid_controller.py   # Tile grid interaction logic
│   ├── leaderboard_state.py # Score display controller
│   ├── menu_state.py        # Main menu controller
│   └── state_controller.py  # State transition manager
├── model/                   # Game data and logic
│   ├── scorekeeper.py       # Score tracking system
│   ├── settings.py          # Game constants and settings
│   └── themes.csv           # Theme configurations
├── view/                    # UI components
│   ├── grid.py              # Game board display
│   ├── tile.py              # Individual tile display
│   └── ui.py                # User interface elements
├── main.py                  # Main entry point
└── requirements.txt         # Project dependencies
```

## Game Configuration

The game can be customized by modifying:
- `settings.py`: Adjust time limit, move limit, grid size, etc.
- `themes.csv`: Add or modify Pokémon themes

## Credits


### Team Members
- Nicole W.
- Jasper Y.

This project was developed as a group project for CS 122: Advanced Python Programming at San Jose State University (Fall 2024).

