# Deck of cards

This is a python package for building or playing card game.


## Installation

This packaged was tested in Python versions 3.8, 3.9 and 3.10. to check your Python vesion,

```shell
python -V
```

To install deckcards,

```python -m pip install deckcards```

## Basic usage

The ```deckcards``` modules provide a framework to implement a game of cards in python. For details on cards and games of cards check out [this wikipedia page](https://en.wikipedia.org/wiki/Standard_52-card_deck).

The two main classes are ```Card``` and ```Deck```.

### ```Card```

An instance of ```Card``` represents a single card. Create a card object providing two parameters: rank and suit. Both string. Valid values for ranks are:

```python
>>> import deckcards as dc
>>> print(cd.Card.ranks)
['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
```

And valids values for suits are either their names or their symbols in [unicode emoji representation](https://en.wikipedia.org/wiki/Playing_cards_in_Unicode#Emoji).

```Card``` have dictionaries to map both ways:

```python
>>> print(dc.Card.suits)
{'club': '♣', 'diamond': '♦', 'heart': '♥', 'spade': '♠'}
>>> print(dc.Card.suits_name)
{'♣': 'club', '♦': 'diamond', '♥': 'heart', '♠': 'spade'}
```

A card objet is only a representation, meaning that it don't present any behavior (method). Create a card:

```python
>>> card = dc.Card('A', '♠')
>>> print(card.rank)
A
>>> print(card.suit)
♠
>>> print(card)
A ♠
>>> card
Card.rank: A, Card.suit: ♠
```
By defult, 'A' is the highest rank:
```python
>>> card.value
13
```

## ```Deck```

An instance of ```Deck``` has four behaviors to build most of popular card games: draw, throw, waste and pick a card, based on three main areas:

**Pack**: cards not in game yet. Also know as draw pile, this area feeds the other two areas.
- **Stock**: cards in game. Although not implemented in this package, you can think of sub-areas of stock as players's hands and as stack (faced down cards in front of players).
- **Waste pile**: cards not in game anymore.

### **Draw**
Action of taking the card from the top of ```pack``` (draw pile) and put it in ```stock```. Stock is where cards in game are stored. A card in game is a card in a player's hand or in table, or stack (shown of not).

### **Throw**
Action of taking a given card from stock and throw it to ```wastepile```. In practice the most common throw is discarding card from a player's hand.

### **Waste**
Action of taking a given card from pack, or the card from it's top, and discard to ```wastepile```. 

### **Pick**
Action of taking a given card from pack, or the card from it's top, and place it in ```stock```.

A fith behavior can be reproduced with method ```deal(self, n_players=2, n_cards=2, standard=True) ```, wich returns a list of ```n_cards``` in each elements, whith length ```n_players```. This function puts all cards in stock. The dealing fashion is standard by default, i.e., one card each hand, each round of dealing.

In src/examples is a script with black Jack implemented. You can run the game:

```python
>> from deckcards.examples import BlackJack
>> game = BlackJack()
>> game.run()
```
```shell
------------
Dealer's cards: |9 ♥||? ?|      -> score: 9
player's cards: |J ♠||5 ♦|      -> score: 15
- Digit s for stand or h for hit:
```
## Authors

* **Vagner Bessa** - [bessavagner](https://github.com/bessavagner)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/bessavagner/deckcards/blob/main/LICENSE) file for details

## Acknowlegments

This project used the template from https://github.com/tomchen/example_pypi_package