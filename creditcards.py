from datetime import datetime
now = datetime.now()
month = now.month


class CreditCard:

    def __init__(self):
        self.name = ""
        self.balance = 0
        self.statment_balance = 0
        self.due_date = ""
        self.points = 0

    def create_card(self):
        while True:
            name = input("Enter card name: ").title()
            self.name = name
            due_date = int(input("Input due date (day) "))
            if due_date > 31:
                print("Day can't be over 31")
                continue
            self.balance = int(input("Enter balance: "))
            self.due_date = due_date
            new_card = {
                "Due Date": self.due_date,
                "Balance": self.balance,
            }
            return name, new_card

    def show_values(self):

        return f"Name: {self.name} has balance of {self.balance} and is due on {self.due_date}/{month}"

    def show_names(self):
        return self.name


class Wallet:

    def __init__(self):
        self.credit_cards = {}

    def add_credit_card(self, name, credit_card):
        self.credit_cards[name] = credit_card

    def remove_credit_card_by_name(self, card_holder_name):
        for card_info in self.credit_cards:
            if card_info['name'] == card_holder_name:
                self.credit_cards.remove(card_info)
                return True  # Card removed successfully
        return False  # Card not found

    def show_cards(self):
        for cards in self.credit_cards:
            print(cards.show_values())

    def show_names_only(self):
        for cards in self.credit_cards:
            print(cards.show_names())
