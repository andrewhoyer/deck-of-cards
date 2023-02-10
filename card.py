class Card:

	def __init__(self, label, suit):
		self.label = label
		self.suit  = suit

		if suit == 'C' or suit == 'S':
			self.color = 'black'
		elif suit == 'H' or suit == 'D':
			self.color = 'red'

		if label == 'J' or label == 'Q' or label == 'K':
			self.face = True
		else:
			self.face = False
		
	
	def name(self, format):
		if format == 'text':
			return self.label + self.suit
			
		elif format == 'symbol':
			return self.label + self.symbol(self.suit)
			
		else:
			return self.label + self.suit


	def symbol(self, suit):
		if suit == 'H':
			return '♡'
		elif suit == 'S':
			return '♤'
		elif suit == 'D':
			return '♢'
		elif suit == 'C':
			return '♧'
		else:
			return ''