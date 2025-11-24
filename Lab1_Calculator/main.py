from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

# Размер окна под мобильное устройство (9:16)
Window.size = (360, 640)

# Чтобы окно всегда стартовало по центру
Window.left = 100
Window.top = 50

class CalculatorLayout(BoxLayout):
    display_text = StringProperty("")

    def press_button(self, value):
        self.display_text += value

    def clear_display(self):
        self.display_text = ""

    def calculate(self):
        try:
            expression = self.display_text.replace("^", "**")
            result = eval(expression)

            # Если результат float
            if isinstance(result, float):

                # Если дробная часть == 0 → выводим как целое
                if result.is_integer():
                    result = int(result)
                else:
                    # Ограничиваем до 6 знаков после запятой
                    result = round(result, 6)

            self.display_text = str(result)

        except ZeroDivisionError:
            self.display_text = "Поверьте мне, повторять подобное - не стоит."
        except Exception:
            self.display_text = "Ошибка!"


class Calculator(App):
    def build(self):
        self.title = "Calculator"
        return CalculatorLayout()


if __name__ == "__main__":
    Calculator().run()
