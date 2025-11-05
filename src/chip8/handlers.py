# A hashtable-based opcode dispatcher for CHIP-8

def cls(chip8, opcode):
    chip8.display.clear()
    chip8.pc += 2

def ret(chip8, opcode):
    chip8.pc = chip8.stack.pop()
    chip8.pc += 2

def jp(chip8, opcode):
    chip8.pc = opcode & 0x0FFF

def call(chip8, opcode):
    chip8.stack.append(chip8.pc)
    chip8.pc = opcode & 0x0FFF

def se_vx_byte(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    nn = opcode & 0x00FF
    chip8.pc += 4 if chip8.V[x] == nn else 2

def sne_vx_byte(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    nn = opcode & 0x00FF
    chip8.pc += 4 if chip8.V[x] != nn else 2

def se_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.pc += 4 if chip8.V[x] == chip8.V[y] else 2

def ld_vx_byte(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    nn = opcode & 0x00FF
    chip8.V[x] = nn
    chip8.pc += 2

def add_vx_byte(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    nn = opcode & 0x00FF
    chip8.V[x] = (chip8.V[x] + nn) & 0xFF
    chip8.pc += 2

def ld_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.V[x] = chip8.V[y]
    chip8.pc += 2

def or_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.V[x] |= chip8.V[y]
    chip8.pc += 2

def and_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.V[x] &= chip8.V[y]
    chip8.pc += 2

def xor_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.V[x] ^= chip8.V[y]
    chip8.pc += 2

def add_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.V[x] += chip8.V[y]
    chip8.V[0xF] = 1 if result > 0xFF else 0
    chip8.V[x] = result & 0xFF
    chip8.pc += 2

def sub_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.V[0xF] = 1 if chip8.V[x] > chip8.V[y] else 0
    chip8.V[x] = (chip8.V[x] - chip8.V[y]) & 0xFF
    chip8.pc += 2

def shr_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.V[0xF] = chip8.V[x] & 0x1
    chip8.V[x] >>= 1
    chip8.pc += 2

def subn_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.V[0xF] = 1 if chip8.V[y] > chip8.V[x] else 0
    chip8.V[x] = (chip8.V[y] - chip8.V[x]) & 0xFF
    chip8.pc += 2

def shl_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.V[0xF] = (chip8.V[x] & 0x80) >> 7
    chip8.V[x] = (chip8.V[x] << 1) & 0xFF
    chip8.pc += 2

def sne_vx_vy(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    y = (opcode & 0x00F0) >> 4
    chip8.pc += 4 if chip8.V[x] != chip8.V[y] else 2

def ld_i_addr(chip8, opcode):
    chip8.I = opcode & 0x0FFF
    chip8.pc += 2

def jp_v0_addr(chip8, opcode):
    chip8.pc = (opcode & 0x0FFF) + chip8.V[0]

def rnd_vx_byte(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    nn = opcode & 0x00FF
    chip8.V[x] = random.randint(0, 255) & nn
    chip8.pc += 2

def drw_vx_vy_nibble(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.delay_timer = chip8.V[x]
    chip8.pc += 2

def skp_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.pc += 4 if chip8.keypad.is_pressed(chip8.V[x]) else 2

def sknp_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.pc += 4 if not chip8.keypad.is_pressed(chip8.V[x]) else 2

def ld_vx_dt(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.V[x] = chip8.delay_timer
    chip8.pc += 2

def ld_vx_k(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    key = chip8.keypad.wait_for_keypress()
    if key is not None:
        chip8.V[x] = key
    chip8.pc += 2

def ld_dt_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.delay_timer = chip8.V[x]
    chip8.pc += 2

def ld_st_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.sound_timer = chip8.V[x]
    chip8.pc += 2

def add_i_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.I = (chip8.I + chip8.V[x]) & 0xFFF
    chip8.pc += 2

def ld_f_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    chip8.I = chip8.V[x] * 5
    chip8.pc += 2

def ld_b_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    value = chip8.V[x]
    chip8.memory[chip8.I] = value // 100
    chip8.memory[chip8.I + 1] = (value // 10) % 10
    chip8.memory[chip8.I + 2] = value % 10
    chip8.pc += 2

def ld_i_vx(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    for i in range(x + 1):
        chip8.memory[chip8.I + i] = chip8.V[i]
    chip8.pc += 2

def ld_vx_i(chip8, opcode):
    x = (opcode & 0x0F00) >> 8
    for i in range(x + 1):
        chip8.V[i] = chip8.memory[chip8.I + i]
    chip8.pc += 2

OPCODES = {
    0x0000: lambda c, o: cls(c, o) if o == 0x00E0 else ret(c, o),
    0x1000: jp,
    0x2000: call,
    0x3000: se_vx_byte,
    0x4000: sne_vx_byte,
    0x5000: se_vx_vy,
    0x6000: ld_vx_byte,
    0x7000: add_vx_byte,
    0x8000: lambda c, o: {
        0x0: ld_vx_vy,
        0x1: or_vx_vy,
        0x2: and_vx_vy,
        0x3: xor_vx_vy,
        0x4: add_vx_vy,
        0x5: sub_vx_vy,
        0x6: shr_vx,
        0x7: subn_vx_vy,
        0xE: shl_vx,
    }[(o & 0x000F)](c, o),
    0x9000: sne_vx_vy,
    0xA000: ld_i_addr,
    0xB000: jp_v0_addr,
    0xC000: rnd_vx_byte,
    0xD000: drw_vx_vy_nibble,
    0xE000: lambda c, o: skp_vx(c, o) if o & 0x00FF == 0x9E else sknp_vx(c, o),
    0xF000: lambda c, o: {
        0x07: ld_vx_dt,
        0x0A: ld_vx_k,
        0x15: ld_dt_vx,
        0x18: ld_st_vx,
        0x1E: add_i_vx,
        0x29: ld_f_vx,
        0x33: ld_b_vx,
        0x55: ld_i_vx,
        0x65: ld_vx_i,
    }[(o & 0x00FF)](c, o),
}
