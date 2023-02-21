# deck-of-cards
A collection of Python classes for managing a deck of standard playing cards.

## Examples

### Deck

#### Creating a Deck

```python
import deck

game_deck = deck.Deck()
```

When you create a deck, it automatically creates a list of standard playing cards.

#### Accessing the deck

The deck can be accessed either as a whole, or by individual card.

To retrieve the entire deck, use:

```python
game_deck.get_all_cards()
```

For example, to output all of the cards in order:

```python
for card in game_deck.get_all_cards():
print(card.get_name('symbol'))
```

To output the name of the card at the top of the deck, access just one card:

```python
card = game_deck.get_card(1)
print(card.get_name('phrase'))
```


#### Shuffling the Deck

The deck can be shuffled at any time and will work with any number of cards, including the case where some cards have been removed from the deck.

```python
game_deck.shuffle()
```

### Card

Each card object can provide information about its suit and label.

#### Card Suit

To get the single character string for the suit (H, S, D, or C) of a card:

```python
card.get_suit()
```

To get the string name (hearts, clubs) for the suit of a card:

```python
card.get_suit_word()
```

#### Card Label

To get the single character string for the label (A, 2, 3 ... J, Q, K) of a card:

```python
card.get_label()
```

To get the string name (ace, three, king) for the label of a card:

```python
card.get_label_word()
```

#### Card name

A card can return a description of the suit and label in a number of formats.

Format options:

- 'text', a string containing the label and suit (AC, 2D, KH)
- 'symbol', a string containing the label, and the suit in symbol form (A♧, 2♢, K♡)
- 'phrase', a string containing the label and suit in a phrase (king of hearts)

```python
print(card.get_name('phrase'))
```
