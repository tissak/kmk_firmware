import board
import digitalio

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

_KEY_CFG = [
    board.D7,  board.A0,   board.A1,   board.A2,  board.A3,
    board.SCK, board.MISO, board.MOSI, board.D10, board.D0,
    board.D2,  board.D3,   board.D4,   board.D5,  board.D6,
    board.D8,  board.D9
]

class KMKKeyboard(_KMKKeyboard):
    coord_mapping = [
    0,   1,  2,  3,  4,           21, 20, 19, 18, 17,
    5,   6,  7,  8,  9,           26, 25, 24, 23, 22,
    10, 11, 12, 13, 14,           31, 30, 29, 28, 27,
                    15, 16,   33, 32
    ]
    data_pin=board.D1
    def __init__(self):
        self.matrix = KeysScanner(pins=_KEY_CFG)
    
