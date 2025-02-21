# Blackjack Nano

A simple command-line Blackjack game written in Python. This project allows users to play a game of Blackjack against a computer dealer.

## Installation

### **Option 1: Install via pip (Recommended)**
If you've uploaded this package to PyPI, users can install it directly using pip:
```sh
pip install blackjack-nano
```

### **Option 2: Run from Source**
If you're running the project from the source code, clone the repository and install any dependencies:
```sh
git clone https://github.com/kpeguero16/blackjack_nano.git
cd blackjack_nano
```

## Running the Game
After installation, you can run the game using:
```sh
blackjack_nano
```
Or if running from source:
```sh
python3 blackjack.py
```

## Development Setup
If you want to contribute or modify the game, follow these steps:
```sh
git clone https://github.com/kpeguero16/blackjack_nano.git
cd blackjack_nano
pip install -r requirements.txt
```
Then, make changes and test your updates!

## Updating the Package
If you make changes and need to update the PyPI package:
```sh
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

