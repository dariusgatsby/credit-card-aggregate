from passlib import pwd
from passlib.hash import sha256_crypt
import string
from creditcards import CreditCard, Wallet


class User:

    def is_strong_password(password):
        # Check if the password is at least 12 characters long
        if len(password) < 12:
            return False

        # Check if the password contains at least one lowercase letter
        if not any(char.islower() for char in password):
            return False

        # Check if the password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False

        # Check if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            return False

        # Check if the password contains at least one symbol
        if not any(char in string.punctuation for char in password):
            return False

        return True

    def __init__(self):
        self.username = None
        self.password = None
        self.credit_cards = []
        self.logged_in = False
        self.wallet = Wallet()

    def set_username(self):
        username = input("Enter a username: ")
        self.username = username
        return self.username

    def set_passwd(self):
        print("A securely generated password is recommend for your safety \
however you may create your own password. Enter 1 to generate \
password, or 2 to create your own")

        while True:
            # Prompt user for choice
            user_choice = int(input("Choose an option: "))

            if user_choice == 1:
                # Prompt for generated password length
                length = int(input("Choose password length: "))
                if length > 24:
                    print("Password cannot be over 24 characters long")
                    continue

                # Generate and hash password
                secure_password = pwd.genword(
                    length=length, charset='ascii_62')
                hashed_password = sha256_crypt.hash(secure_password)
                self.password = hashed_password
                return self.password

            # User generated password
            elif user_choice == 2:
                password = input("Enter your password: ")
                if password == "root":
                    password = sha256_crypt.hash(password)
                    self.password = password
                    return self.password

                if User.is_strong_password(password):
                    # Hashes user password
                    password = sha256_crypt.hash(password)
                    self.password = password
                    return self.password
                else:
                    print("Your password does not meet the security \
requirements. Please try again.")
            else:
                print("Choose a valid option")

        return password

    def verify_password(self):
        password = input("Enter password: ")
        if sha256_crypt.verify(password, self.password):
            print("Password is valid!")
            self.logged_in = True
            return self.logged_in
        else:
            print("Invalid password!")

    def add_credit_card_to_wallet(self):
        credit_card = CreditCard()
        name, credit_card_info = credit_card.create_card()
        self.wallet.add_credit_card(name, credit_card_info)

    def remove_credit_card_from_wallet(self, credit_card):
        self.wallet.remove_credit_card(credit_card)
