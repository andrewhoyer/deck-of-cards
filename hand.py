import random

class Hand:

	def __init__(self):
		self.hand = []
	
	def shuffle(self):
		random.shuffle(self.hand)
	
	def get_all_cards(self):
		return self.hand
	
	def add_card(self, new_card):
		self.hand.append(new_card)

	def get_card(self, position):
		'''returns a Card object. position 1 is the left card in the hand.'''

		if position > 0 and position <= len(self.hand):
			return self.hand[position - 1]
		else:
			return False
	
	def play_card(self, position = 1):
		if position > 0 and len(self.hand) > 0 and position <= len(self.hand):
			return(self.hand.pop(position - 1))
		else:
			return False

