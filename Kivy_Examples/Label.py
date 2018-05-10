from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

# build a label with font size and scalability

class tutorialApp(App):
	def build(self):
		f = FloatLayout()
		s = Scatter()
		l = Label(text = "hi there!", font_size = 200)
		f.add_widget(s)
		s.add_widget(l)
		return f

if __name__ == "__main__":
	tutorialApp().run() 