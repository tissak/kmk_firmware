# Use this extension for showing layer status with three leds

import time
from kmk.extensions import Extension, InvalidExtensionEnvironment
from kmk.keys import make_key
from kmk.extensions.rgb import RGB


class NeoStatusLED(Extension):
    def __init__(
        self,
        led_pin,
        brightness=30,
        brightness_step=5,
        brightness_limit=200,
    ):
        self.led_pin = led_pin        
        self.rgb = RGB(pixel_pin=led_pin, num_pixels=1) 

        self.hues = [
            [30, 90, 21],
            [360, 100, 1],
            [240, 100, 1],
            [120, 100, 1]
        ]

        self._hue = self.hues[0]
        self._saturation = 100
        self._brightness = brightness
        
        self._layer_last = -1
                    
        self.brightness_step = brightness_step
        self.brightness_limit = brightness_limit

        make_key(names=('SLED_INC',), on_press=self._key_led_inc)
        make_key(names=('SLED_DEC',), on_press=self._key_led_dec)

    def _set_rgb(self, layer):
        colors = [
            (0,0,0),
            (255,0,0),
            (0,255,0),
            (0,0,255)
        ]
        self.rgb.brightness = 0.3
        self.rgb.set_rgb_fill(colors[layer])

    def _layer_indicator(self, layer_active, *args, **kwargs):
        '''
        Indicates layer with a neopixel hue        
        '''
        if self._layer_last != layer_active:
            if layer_active == 0:
                self.rgb.off()
            else:
                self._set_rgb(layer_active)
            self._layer_last = layer_active

    def __repr__(self):
        return f'SLED({self._to_dict()})'

    def _to_dict(self):
        return {
            '_hue': self._hue,
            '_saturation': self._saturation,
            '_brightness': self._brightness,
            'brightness_step': self.brightness_step,
            'brightness_limit': self.brightness_limit,
        }

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def set_hsl(self, hsl):
        self.rgb.set_hsv_fill(hsl[0], hsl[1], hsl[2])            

    def during_bootup(self, sandbox):
        '''Cycle hues during boot'''
        for i in range(len(self.hues)):            
            self.set_hsl(self.hues[i])
            time.sleep(0.1)    
        self.set_hsl(self.hues[0])
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        self._layer_indicator(sandbox.active_layers[0])
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):        
        return

    def on_powersave_disable(self, sandbox):        
        return

    def set_brightness(self, percent):
        return

    def increase_brightness(self, step=None):
        if not step:
            self._brightness += self.brightness_step
        else:
            self._brightness += step

        if self._brightness > self.brightness_limit:
            self._brightness = self.brightness_limit

        self.set_brightness(self._brightness)

    def decrease_brightness(self, step=None):
        if not step:
            self._brightness -= self.brightness_step
        else:
            self._brightness -= step

        if self._brightness < 0:
            self._brightness = 0

        self.set_brightness(self._brightness)

    def _key_led_inc(self, *args, **kwargs):
        self.increase_brightness()

    def _key_led_dec(self, *args, **kwargs):
        self.decrease_brightness()
