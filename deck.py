import card
import random

class Deck:

	def reset_deck(self, labels, suits):
		deck = []
		
		for suit in suits:
			for label in labels:
				deck.append(card.Card(label, suit))
  		
		return deck
	
	
	def __init__(self):
		self.suits  = ['H', 'S', 'D', 'C']
		self.labels = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.deck   = self.reset_deck(self.labels, self.suits)
	
	
	def shuffle(self):
		random.shuffle(self.deck)
	
	def get_all_cards(self):
		return self.deck

	def get_card(self, position):
		'''returns a Card object. position 1 is the top card on the deck.'''

		if position > 0 and position <= len(self.deck):
			return self.deck[position - 1]
		else:
			return False


