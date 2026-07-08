from kivy.app import App
from kivy.uix.button import Button

class SultanApp(App):
    def build(self):
        # سلطان بھائی کے لیے ایک سادہ بٹن والی ایپ
        return Button(
            text="Sultan Logic\n\nDemo App Work Success!",
            font_size='24sp',
            background_color=(0, 1, 0, 1) # سبز رنگ کا بٹن
        )

if __name__ == '__main__':
    SultanApp().run()
