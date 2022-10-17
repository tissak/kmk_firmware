import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.quickpin.pro_micro.nice_nano import pinout as pins

# _KEY_CFG = [
#     board.D7,  board.A0,   board.A1,   board.A2,  board.A3,
#     board.SCK, board.MISO, board.MOSI, board.D10, board.D0,
#     board.D2,  board.D3,   board.D4,   board.D5,  board.D6,
#     board.D8,  board.D9
# ]

# 0    board.D0,
# 1    board.D1,
# 2    None,  # GND
# 3    None,  # GND
# 4    board.D2,
# 5    board.D3,
# 6    board.D4,
# 7    board.D5,
# 8    board.D6,
# 9    board.D7,
# 10    board.D8,
# 11    board.D9,
# 12    board.D10,
# 13    board.MOSI,
# 14    board.MISO,
# 15    board.SCK,
# 16    board.A0,
# 17    board.A1,
# 18    board.A2,
# 19    board.A3,

_KEY_CFG = [
    pins[9],   pins[16],   pins[17],   pins[18],  pins[19],
    pins[15],  pins[14],   pins[13],   pins[12],  pins[0],
    pins[4],   pins[5],    pins[6],    pins[7],   pins[8],
    pins[10],  pins[11]
]

class KMKKeyboard(_KMKKeyboard):
    coord_mapping = [
    0,   1,  2,  3,  4,           21, 20, 19, 18, 17,
    5,   6,  7,  8,  9,           26, 25, 24, 23, 22,
    10, 11, 12, 13, 14,           31, 30, 29, 28, 27,
                    15, 16,   33, 32
    ]
    data_pin=pins[1]
    def __init__(self):
        self.matrix = KeysScanner(pins=_KEY_CFG)
    
