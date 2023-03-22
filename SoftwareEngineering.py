# Naji Wehbe
def print_menu():
    print("Menu\n-------------\n1.Encode\n2.Decode\n3.Quit")

def encoder(password):
    encoded = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded += encoded_digit
    return encoded

def main():
    while True:
        print_menu()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to be encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
            print_menu()
            user_input = int(input("Please enter an option: "))

        if user_input == 2:
            #decode()
            print_menu()
            user_input = int(input("Please enter an option: "))

        if user_input == 3:
            break

if __name__ == '__main__':
            main()