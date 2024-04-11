'''
Luca Marinelli
'''


def encoder(password):
    if len(password) != 8 or not password.isdigit():
        return "Invalid password"
    encoded = [(int(char) + 3) % 10 for char in password]
    return ''.join(map(str, encoded))


def decoder(encoded_password):
    # Decoder Function


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = input("\nPlease enter an option: ")

        if choice == "1":
            password = input("Please Enter your password to encode: ")
            encoded_password = encoder(password)
            print(f"Your password has been encoded and stored!\n")
        elif choice == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()