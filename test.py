from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from deep_translator import GoogleTranslator
import re


class EnScreen(FloatLayout):
    def __init__(self, line_count, **kw):
        self.file = open("en.txt", "r")
        self.line_count = line_count

        super(EnScreen, self).__init__(**kw)
        self.box = BoxLayout(orientation='horizontal', spacing=5)

        self.main_label = Label(text=f"{self.get_word(self.line_count)}",
                                bold=True,
                                font_size="30sp",
                                pos_hint={'center_x': 0.5, 'center_y': 0.65},
                                halign="center",
                                color=(0.055, 0.235, 0.541, 1))

        self.main_label_translate = Label(
            text=f"{GoogleTranslator(source='auto', target='ru').translate(self.get_word(self.line_count))}",
            bold=True,
            font_size="30sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            halign="center",
            color=(0.055, 0.235, 0.541, 1))

        self.box.add_widget(Button(text='Previous',
                                   on_press=self.previous,
                                   size_hint=(.5, .25)))
        self.box.add_widget(Button(text='Save',
                                   on_press=self.save,
                                   size_hint=(.5, .25)))
        self.box.add_widget(Button(text='Next',
                                   on_press=self.next,
                                   size_hint=(.5, .25)))
        self.add_widget(self.box)
        self.add_widget(self.main_label_translate)
        self.add_widget(self.main_label)

    def save(self, _):
        """data = {
                "word": self.get_word(self.line_count).replace("\n", ""),
                "translate": GoogleTranslator(source='auto', target='ru').translate(self.get_word(
                                                                                    self.line_count))
        }"""
        with open('en_save.txt', 'a') as outfile:
            outfile.write(f"{self.line_count + 1} {self.get_word(self.line_count)}")

    def previous(self, _):
        self.line_count -= 1
        self.main_label.text = self.get_word(self.line_count)
        self.main_label_translate.text = GoogleTranslator(source='auto', target='ru').translate(self.get_word(
                                                                                                self.line_count))
        return

    def next(self, _):
        self.line_count += 1
        self.main_label.text = self.get_word(self.line_count)
        self.main_label_translate.text = GoogleTranslator(source='auto', target='ru').translate(self.get_word(
                                                                                                self.line_count))
        return

    def get_word(self, lines_to_read):
        self.a_file = open("en.txt")
        self.lines_to_read = lines_to_read
        for position, line in enumerate(self.a_file):
            if position == lines_to_read:
                return line
        self.a_file.close()


class MainApp(App):
    def build(self):
        with open('en_save.txt') as f:
            line_count = 0
            for _ in f:
                line_count += 1
            line_count = int(re.sub('[^0-9]', '', _))
        return EnScreen(line_count)


if __name__ == '__main__':
    MainApp().run()
