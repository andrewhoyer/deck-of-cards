class Card:

	def __init__(self, label, suit):
		self.label = label
		self.label_word = ''
		self.suit  = suit
		self.suit_word = ''

		if suit == 'C' or suit == 'S':
			self.color = 'black'
		elif suit == 'H' or suit == 'D':
			self.color = 'red'
		
		if suit == 'H':
			self.suit_word = 'hearts'
		elif suit == 'S':
			self.suit_word = 'spades'
		elif suit == 'D':
			self.suit_word = 'diamonds'
		elif suit == 'C':
			self.suit_word = 'clubs'

		if label == 'J' or label == 'Q' or label == 'K':
			self.face = True
		else:
			self.face = False
		
		if label == 'A':
			self.label_word = 'ace'
		elif label == '2':
			self.label_word = 'two'
		elif label == '3':
			self.label_word = 'three'
		elif label == '4':
			self.label_word = 'four'
		elif label == '5':
			self.label_word = 'five'
		elif label == '6':
			self.label_word = 'six'
		elif label == '7':
			self.label_word = 'seven'
		elif label == '8':
			self.label_word = 'eight'
		elif label == '9':
			self.label_word = 'nine'
		elif label == '10':
			self.label_word = 'ten'
		elif label == 'J':
			self.label_word = 'jack'
		elif label == 'Q':
			self.label_word = 'queen'
		elif label == 'K':
			self.label_word = 'king'
	
	
	def name(self, format):
		if format == 'text':
			return self.label + self.suit
			
		elif format == 'symbol':
			return self.label + self.symbol(self.suit)
			
		elif format == 'phrase':
			return "{} of {}".format(self.get_label_word(), self.get_suit_word())
			
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

	def get_label_word(self):
		return self.label_word
	
	def get_suit_word(self):
		return self.suit_word

