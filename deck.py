import card

class Deck:

	def reset_deck(self, labels, suits):
  		deck = []
  		
  		for suit in suits:
  			for label in labels:
  				deck.append(card.Card(label, suit))
  		
  		return deck
	
	
	def __init__(self):
		self.suits  = ['H', 'S', 'D', 'C']
		self.labels = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.deck   = self.reset_deck(self.labels, self.suits)
