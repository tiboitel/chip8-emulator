import time

from .display import Display
from .handlers import OPCODES
from .keypad import Keypad
from .constants import FONTSET

class Chip8:
    def __init__(self):
        self.memory = [0] * 4096
        self.V = [0] * 16
        self.I = 0
        self.pc = 0x200
        self.stack = []
        self.delay_timer = 0
        self.sound_timer = 0
        self.display = Display()
        self.keypad = Keypad()
        self.running = False

    def load_fonset():
        fontset_size = 80
        fontset_start_addr = 0x50
        for i, byte in enumerate(FONTSET):
            self.memory[fontset_start_addr + i] = byte

    def load_program(self, program: bytes):
        for i, byte in enumerate(program):
            self.memory[0x200 + i] = byte

    def fetch_opcode(self):
        return self.memory[self.pc] << 8 | self.memory[self.pc + 1]

    def cycle(self):
        opcode = self.fetch_opcode()
        print(f"PC: {self.pc:03X}, Opcode: {opcode:04X}")
        handler = OPCODES.get(opcode & 0xF000, None)
        if handler:
            handler(self, opcode)
        else:
            print(f"Unknown opcode: {opcode:04X}")
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1

    def run(self):
        self.running = True
        while self.running:
            self.cycle()
            time.sleep(1 / 500.0)
