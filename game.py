from hand import Hand
from deck import Deck
from card import Card

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice =""
            while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input(" Please choice 'Hit' or 'Stand' ").lower()
                print()
                while choice not in ['h', 's', 'hit', 'stand']:
                    choice = input("Please enter 'Hit' or 'Stand' or (H/S) ").lower()
                    print()
                if choice in ['h', 'hit']:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_card=True )

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final result ")
            print("Your hand.", player_hand_value)
            print("Dealer hand.", dealer_hand_value)
            print()
            
            self.check_winner(player_hand, dealer_hand, True)

        print("\n Thanks for playing!")


    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print('You basted! Dealer wins! 😥')
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted! You win! 🤟")
                return True
            elif dealer_hand.is_Blackjack() and player_hand.is_Blackjack():
                print("Both player have blackjack! Tie! 😄")
                return True
            elif player_hand.is_Blackjack():
                print("You have blackjack! You win! 🎉")
                return True
            elif dealer_hand.is_Blackjack():
                print("Dealer have blackjack! Dealers wins! 😥")
                return True

        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! 😀")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Game Tie! 🫢")
            else:
                print("Dealers wins! 😥")
            return True
        return False

g = Game()
g.play()