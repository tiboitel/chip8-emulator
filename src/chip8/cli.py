import sys
import pygame
from chip8.core import Chip8
from chip8.renderer import Renderer

KEY_MAP = {
    pygame.K_x: 0x0,
    pygame.K_1: 0x1,
    pygame.K_2: 0x2,
    pygame.K_3: 0x3,
    pygame.K_q: 0x4,
    pygame.K_w: 0x5,
    pygame.K_e: 0x6,
    pygame.K_a: 0x7,
    pygame.K_s: 0x8,
    pygame.K_d: 0x9,
    pygame.K_z: 0xA,
    pygame.K_c: 0xB,
    pygame.K_4: 0xC,
    pygame.K_r: 0xD,
    pygame.K_f: 0xE,
    pygame.K_v: 0xF,
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/rom")
        sys.exit(1)

    rom_path = sys.argv[1]

    # Initialize CHIP-8 system
    chip8 = Chip8()
    renderer = Renderer(chip8.display)

    # Load ROM
    with open(rom_path, "rb") as f:
        program = f.read()
    chip8.load_program(program)

    clock = pygame.time.Clock()
    chip8.running = True

    while chip8.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chip8.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    chip8.running = False
                elif event.key in KEY_MAP:
                    chip8.keypad.press(KEY_MAP[event.key])
            elif event.type == pygame.KEYUP:
                if event.key in KEY_MAP:
                    chip8.keypad.release(KEY_MAP[event.key])

        chip8.cycle()
        renderer.render()
        clock.tick(500)  # Run at ~500Hz, similar to original CHIP-8 speed

    pygame.quit()


if __name__ == "__main__":
    main()

