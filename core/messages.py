class GameMessages:

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

    def generic_win(self, winner, callback):
        user_win = "You win! 😁"
        dealer_wins = "Dealer wins! 😭"
        custom_message = ""
        if winner != self.dealer.owner: custom_message = user_win
        elif winner == self.dealer.owner: custom_message = dealer_wins
        else: custom_message = "Tie!"

        self._show(custom_message)
        callback()

    def blackjack(self, winner, callback):
        user_win = "You have blackjack. You win! 😁."
        dealer_wins = "Dealer has blackjack. Dealer wins! 😭."
        custom_message = user_win if winner.owner != "Dealer" else dealer_wins

        self._show(custom_message)
        callback()

    def busted(self, winner, callback):
        user_win = "Dealer busted. You win! 😁,"
        dealer_wins = "You busted. Dealer wins! 😭."
        custom_message = user_win if winner.owner != "Dealer" else dealer_wins

        self._show(custom_message)
        callback()

    def _show(self, msg):
        print(msg, self._dealer_total_message())
        print(self.dealer.get_details())

    def _dealer_total_message(self): return f"dealer's total was {self.dealer.total()} with next cards:"
