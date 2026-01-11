import random
cards = [
    "A ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥",
    "A ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦",
    "A ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣",
    "A ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠",
    "Joker!"
]

special_cards = [
    "Joker!"
]

def normalize_card_name(card: str) -> str:
    return (
        card.lower()
        .replace(" ", "_")
        .replace("♠", "spades")
        .replace("♥", "hearts")
        .replace("♦", "diamonds")
        .replace("♣", "clubs")
    )

deck = []

def card_throw():
    global deck
    
    if not deck:
        deck = cards.copy()
        random.shuffle(deck)

    card = deck.pop()
    is_special = card in special_cards

    return card, len(deck), is_special

def card_shuffle() -> int:
    deck.clear()
    deck.extend(cards)
    random.shuffle(deck)
    return len(deck)