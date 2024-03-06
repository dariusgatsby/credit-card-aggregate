from users import User
from creditcards import CreditCard, Wallet

user1 = User()

user1.set_username()
user1.set_passwd()
user1.verify_password()
print("Your logged in!")
print(f"Welcome {user1.username}\n")

while user1.logged_in:

    user_choice = input(
        "What would you like to do?\nAdd new card (a)\nDelete a card (del)\nShow Cards (show)\nExit\n ")
    if user_choice == "a":
        user1.add_credit_card_to_wallet()
    if user_choice == "show":
        user1.wallet.show_cards()
    if user_choice == "del":
        user1.wallet.show_names_only()
        card = input("What card would you like to remove?")
        user1.remove_credit_card_from_wallet(card)
    if user_choice == 'exit':
        user1.logged_in = False
