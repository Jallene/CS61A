from kivy.app import App
from kivy.uix.button import Button

# create simple App
# build a button with font, color

class tutorialApp(App):
	def build(self):
		return Button(text = "hi there!", background_color = (0, 0, 1, 1), font_size = 200)

if __name__ == "__main__":
	tutorialApp().run()