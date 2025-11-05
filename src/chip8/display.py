class Display:
    WIDTH = 64
    HEIGHT = 32

    def __init__(self):
        self.pixels = [[0] * self.WIDTH for _ in range(self.HEIGHT)]

    def clear(self):
        self.pixels = [[0] * self.WIDTH for _ in range(self.HEIGHT)]

    def draw_pixel(self, x, y):
        self.pixels[y % self.HEIGHT][x % self.WIDTH] ^= 1
        return not self.pixels[y % self.HEIGHT][x % self.WIDTH]

    def draw_sprite(self, x, y, sprite_bytes):
        collision = False
        for row_index, byte in enumerate(sprite_bytes):
            for bit in range(8):
                sprite_bit = (byte >> (7 - bit)) & 1
                if sprite_bit == 0:
                    continue
                px = (x + bit) % self.width
                py = (y + row_index) % self.height
                idx = py * self.width + px
                if self.pixels[idx] == 1:
                    collision = True
                self.pixels[idx] ^= 1
        return collision
