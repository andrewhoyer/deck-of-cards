class Card:

	def __init__(self, label, suit, deck_rank, suit_rank):
		self.label = label
		self.label_word = ''
		self.suit  = suit
		self.suit_word = ''
		self.deck_rank = deck_rank
		self.suit_rank = suit_rank
		self.color = ''
		
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
	
	
	def get_name(self, format):
		if format == 'text':
			return self.get_label() + self.get_suit()
			
		elif format == 'symbol':
			return self.get_label() + self.get_symbol()
			
		elif format == 'phrase':
			return "{} of {}".format(self.get_label_word(), self.get_suit_word())
			
		else:
			return self.get_label() + self.get_suit()


	def get_symbol(self):
		if self.suit == 'H':
			return '♡'
		elif self.suit == 'S':
			return '♤'
		elif self.suit == 'D':
			return '♢'
		elif self.suit == 'C':
			return '♧'
		else:
			return ''

	def get_label_word(self):
		return self.label_word
	
	def get_suit_word(self):
		return self.suit_word
	
	def get_deck_rank(self):
		return self.deck_rank
	
	def get_suit_rank(self):
		return self.suit_rank

	def get_label(self):
		return self.label
	
	def get_suit(self):
		return self.suit

	def get_color(self):
		return self.color

	def is_face_card(self):
		return self.face
