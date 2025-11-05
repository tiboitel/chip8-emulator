# Install
poetry install

# Run emulator
poetry run python -m chip8.cli examples/PONG-CHIP8.rom --scale 10

# Headless tests
poetry run pytest

