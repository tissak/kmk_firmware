import board
from kb import KMKKeyboard
from kmk.extensions import rgb
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.modtap import ModTap
from kmk.extensions.neostatusled import NeoStatusLED
from kmk.modules.oneshot import OneShot
from kmk.modules.holdtap import HoldTap as _HoldTap

class HoldTap(_HoldTap):
    def ht_activate_hold(self, key, keyboard, *args, **kwargs):
        super()

    def ht_deactivate_hold(self, key, keyboard, *args, **kwargs):
        super()



keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(split_type=SplitType.UART, data_pin=board.D1, use_pio=True, split_side=split_side)

rgb_pixel_pin = board.NEOPIXEL
neoStatusLED = NeoStatusLED(led_pin=rgb_pixel_pin)

layers = Layers()
layers.tap_time = 175

modtap = ModTap()
modtap.tap_time = 175
oneshot = OneShot()

keyboard.modules.append(oneshot)
keyboard.modules.append(modtap)
keyboard.modules.append(layers)
keyboard.modules.append(split)
keyboard.extensions.append(neoStatusLED)

_______ = KC.TRNS
XXXXXXX = KC.NO

L3_Q = KC.LT(3, KC.Q)
L3_P = KC.LT(3, KC.P)
L1_ESC = KC.LT(1, KC.ESC, tap_time=125)
L2_ENT = KC.LT(2, KC.ENT, tap_time=125)

LCAGL = KC.LCTRL(KC.LALT(KC.LGUI(KC.LEFT)))
LCAGD = KC.LCTRL(KC.LALT(KC.LGUI(KC.DOWN)))
LCAGU = KC.LCTRL(KC.LALT(KC.LGUI(KC.UP)))
LCAGR = KC.LCTRL(KC.LALT(KC.LGUI(KC.RIGHT)))
LCAGC = KC.LCTRL(KC.LALT(KC.LGUI(KC.C)))
LCAGM = KC.LCTRL(KC.LALT(KC.LGUI(KC.M)))

# KC.MT(KC.TAP, KC.HOLD, prefer_hold=True, tap_interrupted=False, tap_time=None)

#LCTT_A = KC.MT(KC.A, KC.LCTRL)
LGIT_F = KC.MT(KC.F, KC.LGUI, prefer_hold=False, tap_time=225)
LGIT_J = KC.MT(KC.J, KC.LGUI, prefer_hold=False, tap_time=225)
LSTT_Z = KC.MT(KC.Z, KC.LSFT)
RSTT_SH = KC.MT(KC.SLSH, KC.RSFT)

OS_LCTL = KC.OS(KC.LCTL, tap_time=None)
OS_LSFT = KC.OS(KC.LSFT, tap_time=None)
OS_LGUI = KC.OS(KC.LGUI, tap_time=None)
OS_LALT = KC.OS(KC.LALT, tap_time=None)
OS_LCAG = KC.OS(KC.LCTL(KC.LALT(KC.LGUI)), tap_time=None)

keyboard.keymap = [
    [  # qwerty
        L3_Q,      KC.W,      KC.E,      KC.R,      KC.T,           KC.Y,      KC.U,      KC.I,      KC.O,      L3_P,
        KC.A,      KC.S,      KC.D,      LGIT_F,    KC.G,           KC.H,      LGIT_J,    KC.K,      KC.L,      KC.QUOT,
        LSTT_Z,    KC.X,      KC.C,      KC.V,      KC.B,           KC.N,      KC.M,      KC.COMM,   KC.DOT,    RSTT_SH,
                                         L1_ESC,    KC.SPC,         KC.BSPC,   L2_ENT,
    ],
    [
        KC.N1,     KC.N2,     KC.N3,     KC.N4,     KC.N5,          KC.N6,     KC.N7,     KC.N8,     KC.N9,     KC.N0,
        KC.TAB,    KC.LSFT,   XXXXXXX,   XXXXXXX,   XXXXXXX,        KC.SCLN,   KC.LEFT,   KC.DOWN,   KC.UP,     KC.RIGHT,
        KC.LSFT,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,        XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   KC.GRV,
                                         _______,   KC.LGUI,        _______,   _______,
    ],
    [
        KC.EXLM,   KC.AT,     KC.HASH,   KC.DLR,    KC.PERC,        KC.CIRC,   KC.AMPR,   KC.ASTR,   KC.LPRN,   KC.RPRN, 
        KC.TAB,    KC.LSFT,   XXXXXXX,   XXXXXXX,   XXXXXXX,        KC.MINS,   KC.EQL,    XXXXXXX,   KC.LBRC,   KC.RBRC,
        KC.LSFT,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,        XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   KC.TILD, 
                                         _______,   KC.LGUI,        _______,   _______,
    ],
    [
        _______,   XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,        XXXXXXX,   XXXXXXX,   XXXXXXX,   XXXXXXX,   _______,  
        OS_LCTL,   OS_LALT,   XXXXXXX,   OS_LGUI,   OS_LCAG,        XXXXXXX,   LCAGL,     LCAGD,     LCAGU,     LCAGR,
        OS_LSFT,   XXXXXXX,   LCAGC,     XXXXXXX,   XXXXXXX,        XXXXXXX,   LCAGM,     XXXXXXX,   XXXXXXX,   KC.BSLS,   
                                         _______,   KC.LGUI,        _______,   _______,
    ]
]

if __name__ == '__main__':
    keyboard.go()