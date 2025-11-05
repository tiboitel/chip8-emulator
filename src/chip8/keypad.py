class Keypad:
    def __init__(self):
        self.keys = [0] * 16

    def press(self, key):
        if 0 <= key < 16:
            self.keys[key] = 1

    def release(self, key):
        if 0 <= key < 16:
            self.keys[key] = 0

    def is_pressed(self, key):
        return self.keys[key] == 1

    def wait_for_keypress(self):
        for i, state in enumerate(self.keys):
            if state == 1:
                return i
        return None
