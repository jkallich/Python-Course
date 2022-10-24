import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
# values = {'Two':2, 'Three':2, 'Four':2, 'Five':2, 'Six':2, 'Seven':2, 'Eight':2, 'Nine':2, 'Ten':2, 'Jack':2,'Queen':2, 'King':2, 'Ace':2}
playing = True


class Card:
    '''
    Takes a rank and a suit to create. (EX: Ace of Spades)
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    '''
    Creates a deck of 52 cards. Can list and shuffle the cards.
    '''

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                mycard = Card(suit, rank)
                self.deck.append(mycard)

    def __str__(self):
        mylist = []
        for card in self.deck:
            mylist.append(str(card))

        return '\n'.join(mylist)

    def shuffle(self):
        '''
        Shuffles the deck of 52 cards.
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''
        Returns a card from the shuffled deck and pops it off of the deck so that it cannot be chosen again.
        '''
        deal_card = self.deck.pop()
        return deal_card


class Hand:
    '''
    Calculates the value of a card and adds it to the total value.
    Also adds the card to a list of the player's cards.
    '''

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        '''
        Adds a chosen  the player's card list.
        Also adds the card's value to the player's total value.
        If the new card is an ace, keeps track of it in self.aces.
        '''
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        '''
        Automatically takes away ten from the player's total value if an
        Ace makes the player's total value exceed 21.
        '''

        while self.aces != 0 and self.value > 21:
            self.value -= 10
            self.aces -= 1


class Chips:
    '''
    Keeps track of the player's chips.
    Adds the bet amount to the player's chips if the player wins.
    Subtracts the bet amount from the player's chips if the player loses.
    '''

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self, bet_amt):
        self.total += bet_amt

    def lose_bet(self, bet_amt):
        self.total -= bet_amt


def take_bet(chips):
    '''
    Takes in a bet from the player.
    '''

    while True:
        try:
            player_bet = int(input('Place your bet: '))
            print()
            if player_bet > chips.total:
                print(f'Sorry, you must place a bet that is within your total chips ({chips.total}). ')
        except:
            print('Please enter a number: ')
            continue
        else:
            return player_bet
            print()


def hit(deck, hand):
    '''
    Carries out a hit(draws a new card).
    Adds the new card to the player's hand.
    Adds the new value to the player's total value.
    '''

    hit_card = deck.deal()
    hand.add_card(hit_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    '''
    Asks player if they want to hit or stand. Then performs hit action or breaks out of function if stay.
    '''

    global playing  # to control an upcoming while loop

    while True:

        player_choice = input('Would you like to hit or stand (h/s)?: ')
        print()

        if player_choice == 'h':
            hit(deck, hand)
            # show_some(player,dealer)
            return player_choice
        elif player_choice == 's':
            print("Player stands Dealer's turn")
            playing = False
            return player_choice
        else:
            print("Please enter 'h' or 's': ")


def show_some(player, dealer):
    '''
    Shows all of the player's cards and all except one of the dealer's cards.
    '''

    i = 0
    print("DEALER'S HAND: ")
    for card in dealer.cards:
        if i == 0:
            print('    <card hidden>')
        else:
            print(f'    {card}')
        i += 1
    print()

    print("PLAYER'S HAND: ")
    for card in player.cards:
        print(f'    {card}')
    print(f"Player's Hand = {player.value}\n")


def show_all(player, dealer):
    '''
    Shows all of the player's cards and all of the dealer's cards.
    '''

    print("DEALER'S HAND: ")
    for card in dealer.cards:
        print(f'    {card}')
    print()

    print("PLAYER'S HAND: ")
    for card in player.cards:
        print(f'    {card}')
    print()


def player_busts(player, dealer, player_chips, bet_amt):
    '''
    Ends the game if the player busts.
    '''

    player_chips.lose_bet(bet_amt)

    print("\n----- Player Busts -----")
    show_all(player, dealer)
    print(f"Dealer's Hand = {dealer.value}")
    print(f"Player's Hand = {player.value}\n")


#     print(f"Player's winnings stand at {player_chips.total}")

def player_wins(player, dealer, player_chips, bet_amt):
    '''
    Ends the game if the player's total value is greater than the dealer's total value
    '''
    player_chips.win_bet(bet_amt)
    print("\n----- Player Wins -----")
    # show_all(player, dealer)
    print(f"Dealer's Hand = {dealer.value}")
    print(f"Player's Hand = {player.value}\n")


#     print(f"Player's winnings stand at {player_chips.total}")

def dealer_busts(player, dealer, player_chips, bet_amt):
    '''
    Ends the game if the dealer busts.
    '''

    player_chips.win_bet(bet_amt)
    print("\n----- Dealer Busts -----")
    # show_all(player, dealer)
    print(f"Dealer's Hand = {dealer.value}")
    print(f"Player's Hand = {player.value}\n")


#     print(f"Player's winnings stand at {player_chips.total}")

def dealer_wins(player, dealer, player_chips, bet_amt):
    '''
    Ends the game if the dealer's total value if greater than the player's total value.
    '''

    player_chips.lose_bet(bet_amt)
    print("\n----- Dealer Wins -----")
    # show_all(player, dealer)
    print(f"Dealer's Hand = {dealer.value}")
    print(f"Player's Hand = {player.value}\n")


#     print(f"Player's winnings stand at {player_chips.total}")


#     def push():
def tie(player, dealer, player_chips, bet_amt):
    '''
    Ends the game if both the dealer and player have gone and their total values are the same;
    ends game if there is a tie
    '''
    print("\n----- Tie -----")
    # show_all(player, dealer)
    print(f"Dealer's Hand = {dealer.value}")
    print(f"Player's Hand = {player.value}\n")
#     print(f"Player's winnings stand at {player_chips.total}")

def players_turn(deck, player, dealer, player_chips, bet_amt):
    while True:
        # Prompt for Player to Hit or Stand
        player_choice = hit_or_stand(deck, player)

        if player.value > 21:
            show_some(player, dealer)
            player_busts(player, dealer, player_chips, bet_amt)
            # playing = False
            break
        if player_choice == 's':
            flag = True
            break

        # Show cards (but keep one dealer card hidden)
        if player_choice == 'h':
            show_some(player, dealer)

    return player_choice


## ------------------------------------------------------------------------------ ##


def blackjack():

    # Set up the Player's chips
    player_chips = Chips()

    while True:

        global playing
        playing = True

        # Print an opening statement
        print('----------Welcome to Blackjack!----------')
        print('Get as close to 21 as you can without going over.')
        print('Dealer hits until he reaches 17. Aces count as 1 or 11.')
        print()
        print(f'You have {player_chips.total} chips. ')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player = Hand()
        dealer = Hand()

        player.add_card(deck.deal())
        player.add_card(deck.deal())

        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())

        #     # Set up the Player's chips
        #     player_chips = Chips()

        # Prompt the Player for their bet
        print()
        bet_amt = take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # while playing:  # recall this variable from our hit_or_stand function

        player_choice = players_turn(deck, player, dealer, player_chips,bet_amt)

        if player_choice == 's':

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            while dealer.value < 17:
                dealer.add_card(deck.deal())

            # Show all cards
            show_all(player,dealer)

            # Run different winning scenarios
            if dealer.value > 21:
                dealer_busts(player, dealer, player_chips, bet_amt)
            elif dealer.value > player.value:
                dealer_wins(player, dealer, player_chips, bet_amt)
            elif player.value > dealer.value:
                player_wins(player, dealer, player_chips, bet_amt)
            elif player.value == dealer.value:
                tie(player, dealer, player_chips, bet_amt)


        # Inform Player of their chips total
        print(f"Player's winnings stand at {player_chips.total}")

        # Ask to play again
        play_again = input('Would you like to play again (y/n)? If you do, your chips will be saved: ')
        if play_again == 'y':
            print()
            print()
            continue
        else:
            print('Thank you for playing! ')
            break

blackjack()
