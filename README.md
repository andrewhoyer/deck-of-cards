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

### Dealing a Card

One card can be dealt from the top of the deck using the deal_card() function. The top card object is removed from the Deck, and returned.

```python
top_card = game_deck.deal_card()
```

For ordering of cards, and other sorting and filtering, create a Hand object and add cards to it.

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
#### Card position

In order to calculate the rank and order of cards, each card in the deck is assigned a value for its position in its suit, as well as within the deck.

The suits are ranked from highest to lowest: S, H, D, C.

The cards are ranked from highest to lowest: A being the highest, 2 being the lowest

Examples:

2C has a deck rank of 1
AS has a deck rank of 52
2D has a deck rank of 14
JH has a deck rank of 36

2D has a suit rank of 1
AD has a suit rank of 13
5C has a suit rank of 4
KC has a suit rank of 12

To retrieve the rank of a card within the deck:

```python
card.get_deck_rank()
```

To retrieve the rank of a card within its suite:

```python
card.get_suit_rank()
```
### Hand

A hand can be used to store a subset of cards. The functions available to it have some similaries to a deck, plus the ability to sort and filter based on suit, and the rank for suit and deck.

#### Creating a Hand

```python
import hand

game_hand = hand.Hand()
```

When you create a hand, it contains no cards.

To retrieve the entire hand, use:

```python
game_hand.get_all_cards()
```

For example, to output all of the cards in order:

```python
for card in game_hand.get_all_cards():
    print(card.get_name('phrase'))
```

To output the name of the first card in the hand, access a single card:

```python
card = game_hand.get_card(1)
print(card.get_name('phrase'))
```

#### Shuffling the Hand

Not common for games, shuffling is made available here for use in statistical tests. The hand can be shuffled at any time and will work with any number of cards.

```python
game_hand.shuffle()
```

### Playing a Card

One card can be played from the hand using the play_card() function. The card object is removed from the hand, and returned.

```python
played_card = game_hand.play_card(1)
```

The play_card() function takes a value indicating the position of the card in the hand. Position 1 is the leftmost card. If no value is passed, the card in position 1 is played. If the hand is empty, or a card is requested outside the range in the hand, the return value will be False.
