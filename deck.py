import card
import random

class Deck:

	def reset_deck(self, labels, suits):
		deck = []
		
		deck_position = 1
		for suit in suits:
			suit_position = 1
			for label in labels:
				deck.append(card.Card(label, suit, deck_position, suit_position))
				suit_position = suit_position + 1
				deck_position = deck_position + 1
  		
		return deck
	
	
	def __init__(self):

		# The order of suits and labels is specific for card ranking
		self.suits  = ['C', 'D', 'H', 'S']
		self.labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
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
	
	def deal_card(self):
		return(self.deck.pop(0))

