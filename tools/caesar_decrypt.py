def caesar_decrypt(text, shift):
    def shift_char(c):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base - shift) % 26 + base)
        return c
    return ''.join(shift_char(c) for c in text)
