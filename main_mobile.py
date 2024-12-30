from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        # Main layout
        self.main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Display for results
        self.result = TextInput(
            font_size=36,
            readonly=True,
            halign="right",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.main_layout.add_widget(self.result)

        # Button layout
        button_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.8))

        # Buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "="
        ]

        for button in buttons:
            button_layout.add_widget(
                Button(
                    text=button,
                    font_size=24,
                    on_press=self.on_button_press
                )
            )

        self.main_layout.add_widget(button_layout)
        return self.main_layout

    def on_button_press(self, instance):
        current_text = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = ""
        elif button_text == "=":
            try:
                # Evaluate the expression
                self.result.text = str(eval(current_text))
            except ZeroDivisionError:
                self.result.text = "Error: Division by Zero"
            except Exception:
                self.result.text = "Error"
        else:
            # Append the button's text to the current text
            self.result.text += button_text

if __name__ == "__main__":
    CalculatorApp().run()
