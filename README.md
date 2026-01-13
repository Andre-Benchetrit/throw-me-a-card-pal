# throw-me-a-card-pal-
A customized bot for dice and cards throwing, with sound effects and others features to make a better experience playing Sacramento RPG.

## Features

- 🎲 Dice rolling with support for multiple dice types and modifiers (e.g., `?2d6+3`, `?1d20`)
- 🃏 Card drawing from a standard 52-card deck plus Joker
- 🎵 Sound effects for special cards (Jokers)
- 💰 Coin flipping functionality
- 🔄 Deck shuffling capability

## Installation

### Prerequisites

Before installing the bot, you need to have the following installed on your system:

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

On Windows, you'll also need to install **FFmpeg** for audio playback. On Linux/macOS, FFmpeg can be installed via package managers (see below).

### Installing FFmpeg

#### Windows
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract the archive to a folder (e.g., `C:\ffmpeg`)
3. Add the `bin` folder to your system PATH environment variable

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS
```bash
brew install ffmpeg
```

### Setting up the Bot

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/throw-me-a-card-pal-.git
   cd throw-me-a-card-pal-
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your Discord bot token:
   ```env
   TOKEN=your_discord_bot_token_here
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

Once the bot is running and connected to your Discord server, you can use the following commands (all commands use `?` as prefix):

### Card Commands
- `?card` - Draws a random card from the deck
- `?shuffle` - Shuffles the deck, returning all cards to the deck
<img width="1029" height="689" alt="image" src="https://github.com/user-attachments/assets/6f08cb21-1423-43f1-a123-5c79e62c8f3e" />


### Dice Commands
- `?1d20` - Rolls a single 20-sided die
- `?2d6+3` - Rolls 2 six-sided dice and adds 3 to the total
- `?d100` - Rolls a 100-sided die
- `?2d20kh` - Rolls 2 twenty-sided dice and keeps the highest value
- `?4d6kl3` - Rolls 4 six-sided dice and keeps the lowest 3 values
<img width="540" height="315" alt="image" src="https://github.com/user-attachments/assets/6a27d283-1d92-446e-b8dd-c334672e6d42" />

### Coin Command
- `?coin` - Flips a coin (results in "Heads" or "Tails")
<img width="986" height="669" alt="image" src="https://github.com/user-attachments/assets/d050bdf6-37b4-447d-8a7e-a125e4ccbb43" />


## Configuration

The bot has configurable limits defined in `core/config.py`:
- `MAX_DICE`: Maximum number of dice that can be rolled at once (default: 20)
- `MAX_FACES`: Maximum number of faces on a die (default: 100)

## Audio Support

The bot plays sound effects when special cards are drawn (Jokers). These sounds are stored in the `music/` directory. To add a sound effect for a card, create an MP3 file named after the card using underscores instead of spaces (e.g., `joker!.mp3` for "Joker!" card).

For audio to work properly, ensure that FFmpeg is installed and accessible from your system PATH, and that you have PyNaCl installed (which is included in requirements.txt).

## Contributing

Feel free to submit issues and enhancement requests via GitHub. Pull requests are welcome!
