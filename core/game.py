from core import deck, hand, messages

Deck = deck.Deck
Hand = hand.Hand
Messages = messages.GameMessages

class Game():

    def __init__(self):
        self.deck = Deck()

    def start(self):
        self._create_hands()
        self._deal_cards(2)

    def _deal_cards(self, quantity: int = 1):
        while quantity > 0:
            self.dealer_hand.add_card(self._get_random_card())
            self.player_hand.add_card(self._get_random_card())
            quantity -= 1
        self._ask_to_continue()


    def _ask_to_continue(self, stand = False):
        self._show_status()
        there_is_winner = self._check_winner(stand)
        if there_is_winner: return
        
        try:
            self._show_question_to_continue()
        except:
            return print("Ended")

    def _show_question_to_continue(self):
        user_input = input("Please choose 'Hit' or 'Stand' type (h/s):")

        if user_input.lower() == "h":
            self._deal_cards()
        elif user_input.lower() == "s":
            self._check_winner(True)
        else:
            print("Option not recognized, please type either 'h' or 's'")
            return self._show_question_to_continue()
            
    def _check_winner(self, stand = False):
        dealer = self.dealer_hand
        player = self.player_hand
        dealer_total = dealer.total()
        player_total = player.total()
        there_is_winner = True

        if not stand:
            if dealer_total > 21:
                self.messages.busted(player, self._play_again)
            elif player_total > 21:
                self.messages.busted(dealer, self._play_again)
            elif dealer.is_blackjack():
                self.messages.blackjack(dealer, self._play_again)
            elif player.is_blackjack():
                self.messages.blackjack(player, self._play_again)
            else:
                there_is_winner = False
        else:
            if dealer_total > player_total:
                self.messages.generic_win(dealer, self._play_again)
            elif dealer_total < player_total:
                self.messages.generic_win(player, self._play_again)
            elif dealer_total == player_total:
                self.messages.generic_win("", self._play_again)
            else:
                there_is_winner = False
                
        return there_is_winner

    def _create_hands(self):
        self.dealer_hand = Hand("Dealer")
        self.player_hand = Hand("Player")
        self.messages = Messages(self.player_hand, self.dealer_hand)

    def _show_hands(self, partial = False):
        return partial

    def _play_again(self):
        self.player_hand.clear_card()
        self.dealer_hand.clear_card()
        self.deck.build()
        print("...")

    def _show_status(self):
        print("----------------------------")
        print("            Status          ")
        print("----------------------------")
        print(f"\nPlayer hand value: \n{self.player_hand.get_details()}Total Value: {self.player_hand.total()}\n")
        print("----------------------------")
        print(f"\nDealer hand value: \n{self.dealer_hand.get_details(True)}Total Value: {self.dealer_hand.total(True)}\n")
        print("----------------------------")

    def _get_random_card(self):
        random_card = self.deck._get_random_card()
        return random_card

def bootstrap (callback):
    game = Game()
    game.start()
    callback(game)