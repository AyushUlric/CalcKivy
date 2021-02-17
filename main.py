from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.toast import toast
from kivy.properties import StringProperty

class Calculator(MDApp):
	TextLabel = StringProperty('')
	SecondaryTextLabel = StringProperty('')
	to_eval = ''
	bracket_opened = False
	evaluate = False

	def build(self):
		master = Builder.load_file('main.kv')
		return master

	def updateLabel(self, val):
		if 'numeric' in val :
			number = val.split('-')[1]
			if number == "0":
				if len(self.TextLabel)==0 or (len(self.TextLabel) != self.TextLabel.count('0')):
					self.TextLabel += number
					self.to_eval += number
			else:
				if len(self.TextLabel) == self.TextLabel.count('0'):
					self.TextLabel = ''
					self.to_eval = ''
				self.TextLabel += number
				self.to_eval += number

		elif val=='alpha-c':
			self.TextLabel = ''
			self.to_eval = ''
			self.SecondaryTextLabel = ''
			self.evaluate = False

		elif val=='code-brackets':
			if self.bracket_opened:
				self.TextLabel += ')'
				self.to_eval += ')'
				self.bracket_opened = False
			else:
				self.TextLabel += '('
				self.to_eval += '('
				self.bracket_opened = True

		elif val=='percent-outline' and len(self.TextLabel)!=0:
			self.evaluate = True
			self.TextLabel += '[color=#03ff00]%[/color]'
			self.to_eval += '%'

		elif val=='division' and len(self.TextLabel)!=0:
			self.evaluate = True
			self.TextLabel += '[color=#03ff00]/[/color]'
			self.to_eval += '/'

		elif val=='close' and len(self.TextLabel)!=0:
			self.evaluate = True
			self.TextLabel += '[color=#03ff00]*[/color]'
			self.to_eval += '*'

		elif val=='minus' and len(self.TextLabel)!=0:
			self.evaluate = True
			self.TextLabel += '[color=#03ff00]-[/color]'
			self.to_eval += '-'

		elif val=='plus' and len(self.TextLabel)!=0:
			self.evaluate = True
			self.TextLabel += '[color=#03ff00]+[/color]'
			self.to_eval += '+'

		elif val=='equal' and len(self.TextLabel)!=0:
			try:
				self.TextLabel = str(eval(self.to_eval))
				self.SecondaryTextLabel = ''
				self.evaluate = False
			except:
				toast('Invalid format!')

		elif val=='decimal' and len(self.TextLabel)!=0:
			self.TextLabel += '.'
			self.to_eval += '.'

		elif val=='plus-minus-variant' and len(self.TextLabel)!=0:
			last = self.to_eval[-1]
			if last == "+":
				self.TextLabel += '[color=#03ff00]-[/color]'
				self.to_eval += '-'
			elif last == '-':
				self.TextLabel += '[color=#03ff00]+[/color]'
				self.to_eval += '+'
			else:
				self.TextLabel += '[color=#03ff00]-[/color]'
				self.to_eval += '-'

		if self.evaluate:
			try:
				self.SecondaryTextLabel = str(eval(self.to_eval))
			except:
				self.SecondaryTextLabel = 'E'

	def backspace(self):
		if len(self.TextLabel)!=0:
			last = self.TextLabel[-1]
			if last == ']':
				self.TextLabel = self.TextLabel[:-24]
				self.to_eval = self.to_eval[:-1]
			else:
				self.TextLabel = self.TextLabel[:-1]
				self.to_eval = self.to_eval[:-1]

			if self.evaluate:
				try:
					self.SecondaryTextLabel = str(eval(self.to_eval))
				except:
					self.SecondaryTextLabel = ''
			if len(self.TextLabel)==0:
				self.bracket_opened = False

Calculator().run()
