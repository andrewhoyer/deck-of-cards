# deck-of-cards
A collection of Python classes for managing a deck of standard playing cards.

## Examples

### Creating a Deck

When you create a deck, it automatically creates an array of cards.

```python
import deck

game_deck = deck.Deck()
```

The array of cards can be accessed using the deck variable.

### Shuffling the Deck

The deck can be shuffled at any time and will work with any number of cards, in the case where some have been removed from the deck.

```python
game_deck.shuffle()
```

### Card details

Each card object in the deck has the following pieces of information:

- suit, a single character string (H, S, D, or C)
- label, a single character string (A, 2, 3 ... J, Q, K)
- suit_word, a string name for the suit (hearts, clubs)
- labelword, a string name for the label (ace, three, king)

To get the suit of the first card in the deck:

```python
print(game_deck.deck[0].suit)
```

### Card name

A card can return a description of the suit and label in a number of formats.

card.name(<format>)

Format options:

- 'text', a string containing the label and suit (AC, 2D, KH)
- 'symbol', a string containing the label, and the suit in symbol form (A♧, 2♢, K♡)
- 'phrase', a string containing the label and suit in a phrase (king of hearts)

```python
print(game_deck.deck[0].name('phrase'))
```
